from django.contrib import admin
from .models import Job

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'location', 'salary', 'posted_date', 'closing_date')
    search_fields = ('title', 'company__name', 'location')
    list_filter = ('posted_date', 'closing_date')
    ordering = ('-posted_date',)
