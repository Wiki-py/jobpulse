from django.db import models

# Create your models here.
class Company(models.Model):
    """
    Model representing a company.
    """
# Define choices for country and industry
    #country choices
    COUNTRY = [
        ('KENYA', 'KENYA'),
        ('Tanzania', 'Tanzania'),
        ('Rwanda', 'Rwanda'),
        ('Burundi', 'Burundi'),
        ('South Africa', 'South Africa'),
        ('Nigeria', 'Nigeria'),
        ('Ghana', 'Ghana'),
        ('UGA', 'Uganda'),
        ('USA', 'United States'),
        ('UK', 'United Kingdom'),
        ('Canada', 'Canada'),
        ('India', 'India'),
        ('Australia', 'Australia'),
        ('Germany', 'Germany'),
        ('France', 'France'),
        ('Other', 'Other'),
    ]
    #company industry choices
    INDUSTRY = [
        ('IT', 'Information Technology'),
        ('Finance', 'Finance'),
        ('Healthcare', 'Healthcare'),
        ('Education', 'Education'),
        ('Retail', 'Retail'),
        ('Manufacturing', 'Manufacturing'),
        ('Other', 'Other'),
    ]
    #company details
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    industry = models.CharField(max_length=50, choices=INDUSTRY, default='Other')
    established_date = models.DateField(blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, choices=COUNTRY, default=None)
    logo = models.ImageField(upload_to='company_logos/', blank=True, null=True)

    #communication
    website = models.URLField(blank=True, null=True)
    email  = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    fax = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.name
