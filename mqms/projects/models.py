from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings

class Project(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    client_name = models.CharField(max_length=200, blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='created_projects')

    def __str__(self):
        return self.name
