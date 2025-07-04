from django.db import models
from django.utils import timezone

class Job(models.Model):
    """
    Model representing a job posting.
    """
    title = models.CharField(max_length=255)
    description = models.TextField()
    company = models.ForeignKey('company.Company', on_delete=models.CASCADE)
    location = models.CharField(max_length=255, blank=True, null=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    posted_date = models.DateTimeField(default=timezone.now)
    closing_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

# Create your models here.
