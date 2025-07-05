from django.shortcuts import render

def register_recruiter(request):
    return render(request, 'register_recruiter.html')

def recruiter_login(request):
    return render(request, 'recruiter_login.html')

def company_home(request):
    return render(request, 'recriuter_dashboard.html')

# Create your views here.
