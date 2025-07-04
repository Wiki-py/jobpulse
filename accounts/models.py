from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    """
    Custom user model that extends the default Django user model.
    """
    pasport_photo = models.ImageField(upload_to='passport_photos/', blank=True, null=True)
    
    def __str__(self):
        return self.username  # or any other field you want to represent the user
