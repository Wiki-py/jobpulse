from django.shortcuts import render


def company_home(request):
    return render(request, 'company_dashboard.html')

# Create your views here.
