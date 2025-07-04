from django.urls import path
from . import views


urlpatterns = [
    path('company/company_dashboard.html', views.company_home, name='Recuriter_Dashboard'),
]
