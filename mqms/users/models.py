from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Engineer', 'Engineer'),
        ('Inspector', 'Quality Inspector'),
        ('Client', 'Client'),
        ('Technician', 'Technician'),
    ]
    role = models.CharField(max_length=30, choices=ROLE_CHOICES, default='Technician')

    def __str__(self):
        return f"{self.username} ({self.role})"
