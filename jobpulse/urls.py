from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    #job urls
    path('', include('job.urls')),
    path('/job/', include('job.urls')),

    #company urls
    path('', include('company.urls')),
]
