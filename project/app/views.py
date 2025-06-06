from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Q
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.core.paginator import Paginator
from django.contrib import messages
from django.core.cache import cache
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import get_backends

from .models import Job, JobApplication, UserProfile
from .forms import (
    CustomUserCreationForm,
    ProfileSetupForm,
    JobApplicationForm,
)
from .recommender import get_content_based_recommendations


# Profile view with recommendations and applications
class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Ensure a UserProfile exists
        profile, created = UserProfile.objects.get_or_create(user=self.request.user)
        context['profile'] = profile

        # Fetch user's job applications
        context['applications'] = JobApplication.objects.filter(
            user=self.request.user
        ).select_related('job')

        # Fetch job recommendations using BERT model with caching
        cache_key = f"user_recommendations_{self.request.user.id}"
        recommended_jobs = cache.get(cache_key)

        if recommended_jobs is None:
            recommended_jobs = get_content_based_recommendations(self.request.user.id)
            cache.set(cache_key, recommended_jobs, timeout=3600)  # Cache for 1 hour

        context['recommended_jobs'] = recommended_jobs
        return context


# Job listing view with filters, sorting, and pagination
def job_list(request):
    query = request.GET.get('q', '').strip()
    location = request.GET.get('location', '').strip()
    category = request.GET.get('category', '').strip()
    salary = request.GET.get('salary', None)
    sort_by = request.GET.get('sort_by', '-created_date')

    cache_key = f"jobs_{query}_{location}_{category}_{salary}_{sort_by}"
    jobs = cache.get(cache_key)

    if not jobs:
        jobs = Job.objects.only('id', 'title', 'location', 'category', 'salary', 'created_date').all()

        if query:
            jobs = jobs.filter(Q(title__icontains=query) | Q(location__icontains=query) | Q(description__icontains=query))

        if location:
            jobs = jobs.filter(location__iexact=location)

        if category:
            jobs = jobs.filter(category__iexact=category)

        if salary:
            try:
                salary = float(salary)
                jobs = jobs.filter(salary__gte=salary)
            except ValueError:
                messages.error(request, "Invalid salary input.")

        if sort_by in ['created_date', '-created_date', 'salary', '-salary']:
            jobs = jobs.order_by(sort_by)

        cache.set(cache_key, jobs, timeout=3600)

    paginator = Paginator(jobs, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'job_list.html', {
        'jobs': page_obj,
        'locations': Job.objects.values_list('location', flat=True).distinct(),
        'categories': Job.objects.values_list('category', flat=True).distinct(),
        'salaries': Job.objects.values_list('salary', flat=True).distinct(),
        'selected_location': location,
        'selected_category': category,
        'selected_salary': salary,
        'sort_by': sort_by,
    })


# Job detail view
@login_required
def job_detail(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    similar_jobs = Job.objects.filter(category=job.category).exclude(pk=job_id)[:15]

    # Fetch job recommendations
    cache_key = f"user_recommendations_{request.user.id}"
    recommended_jobs = cache.get(cache_key)
    if recommended_jobs is None:
        recommended_jobs = get_content_based_recommendations(request.user.id)
        cache.set(cache_key, recommended_jobs, timeout=3600)

    return render(request, 'job_detail.html', {
        'job': job,
        'similar_jobs': similar_jobs,
        'recommended_jobs': recommended_jobs,
    })


# Apply for a job
@login_required
def apply_for_job(request, job_id):
    job = get_object_or_404(Job, pk=job_id)

    if JobApplication.objects.filter(user=request.user, job=job).exists():
        messages.warning(request, f"You have already applied for the job: {job.title}.")
        return redirect('job_detail', job_id=job_id)

    if request.method == 'POST':
        form = JobApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.user = request.user
            application.job = job
            application.save()
            messages.success(request, f"You have successfully applied for the job: {job.title}.")
            return redirect('job_applied')
    else:
        form = JobApplicationForm()
    return render(request, 'apply_for_job.html', {'form': form, 'job': job})


# Register new user
def register(request):
    form = CustomUserCreationForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        backend = get_backends()[0]
        user.backend = f"{backend.__module__}.{backend.__class__.__name__}"
        login(request, user)
        messages.success(request, "Registration successful. Please set up your profile.")
        return redirect('setup_profile')
    return render(request, 'register.html', {'form': form})


# Setup profile after registration
@login_required
def setup_profile(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = ProfileSetupForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile has been updated successfully.")
            return redirect('job_list')
    else:
        form = ProfileSetupForm(instance=profile)
    return render(request, 'setup_profile.html', {'form': form})


# Edit profile view
@login_required
def edit_profile(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = ProfileSetupForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile has been updated successfully.")
            return redirect('profile')
    else:
        form = ProfileSetupForm(instance=profile)

    return render(request, 'edit_profile.html', {'form': form})


# Page after job application
@login_required
def job_applied(request):
    return render(request, 'job_applied.html')


# Custom login/logout views
class CustomLoginView(LoginView):
    template_name = 'login.html'
    authentication_form = AuthenticationForm


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')
