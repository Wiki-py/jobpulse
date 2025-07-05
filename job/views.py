from django.shortcuts import render

def job_home(request):
    return render(request, 'job_list.html')

def index(request):
    return render(request, 'index.html')
# Create your views here.
