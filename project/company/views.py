from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import CompanyRegistrationForm
from .models import CompanyProfile


def company_register(request):
    if request.method == 'POST':
        form = CompanyRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, user)

            # ✅ Automatically create CompanyProfile if needed
            CompanyProfile.objects.get_or_create(user=user)
            return redirect('company_dashboard')
    else:
        form = CompanyRegistrationForm()
    return render(request, 'company/register.html', {'form': form})


def company_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user:
            try:
                # ✅ Check if user has an associated company profile
                _ = user.companyprofile
                login(request, user)
                return redirect('company_dashboard')
            except CompanyProfile.DoesNotExist:
                messages.error(request, "This account is not registered as a company.")
        else:
            messages.error(request, "Invalid credentials")
    return render(request, 'company/login.html')


@login_required
def company_dashboard(request):
    try:
        company_profile = request.user.companyprofile
    except CompanyProfile.DoesNotExist:
        return redirect('company_register')
    return render(request, 'company/dashboard.html', {'company_profile': company_profile})


def company_logout(request):
    logout(request)
    return redirect('company_login')




