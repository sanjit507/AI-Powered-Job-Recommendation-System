from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
from .views import ProfileView
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path


urlpatterns = [
    # Job Listings
    path('', views.job_list, name='job_list'),
    
    # Job Detail Page
    path('job/<int:job_id>/', views.job_detail, name='job_detail'),
    
    # Apply for Job
    path('job/<int:job_id>/apply/', views.apply_for_job, name='apply_for_job'),
    
    # Job Applied Confirmation Page
    path('job/applied/', views.job_applied, name='job_applied'),
    
    # Register User
    path('register/', views.register, name='register'),
    
    # Setup Profile
    path('setup-profile/', views.setup_profile, name='setup_profile'),
    
    # Edit Profile
    path('edit-profile/', views.edit_profile, name='edit_profile'),

    # Profile Page
    path('profile/', ProfileView.as_view(), name='profile'),
    
    # Login User
    path('login/', views.CustomLoginView.as_view(), name='login'),
    
    # Logout User
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),

    path('auth/', include('social_django.urls', namespace='social')),

  


    
    # Change Password
    path(
        'password_change/',
        auth_views.PasswordChangeView.as_view(template_name='password_change.html'),
        name='password_change'
    ),
    
    # Password Change Done
    path(
        'password_change/done/',
        auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'),
        name='password_change_done'
    ),
]

# Serve static files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
