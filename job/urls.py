from django.urls import path
from . import views

urlpatterns  = [
    path('', views.index, name = 'Home'),
    path('job_list.html', views.job_home, name='Dashboard'),
]