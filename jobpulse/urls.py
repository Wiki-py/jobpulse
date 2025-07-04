from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('job/', include('job.urls')),
    path('company/', include('company.urls')),
]
