from django.contrib import admin
from .models import Company

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'industry', 'established_date', 'location', 'website')
    search_fields = ('name', 'industry', 'location')
    list_filter = ('industry', 'established_date')
    ordering = ('name',)

# Register your models here.
