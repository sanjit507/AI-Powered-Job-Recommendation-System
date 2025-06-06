from django.urls import path
from company.views import company_register

from . import views

urlpatterns = [
    path('register/', views.company_register, name='company_register'),
    path('login/', views.company_login, name='company_login'),
    path('dashboard/', views.company_dashboard, name='company_dashboard'),
    path('logout/', views.company_logout, name='company_logout'),

]
