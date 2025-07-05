from django.urls import path
from . import views


urlpatterns = [
    path('register_recruiter.html', views.register_recruiter, name='Register Recruiter'),
    path('recruiter_login.html', views.recruiter_login, name = 'Recruiter Login'),
    path('recriuter_dashboard.html', views.company_home, name='Dashboard'),
]
