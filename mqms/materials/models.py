from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings
from projects.models import Project

class MaterialType(models.Model):
    name = models.CharField(max_length=100)  # e.g., Concrete, Steel, Aggregate
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class MaterialTest(models.Model):
    TEST_TYPES = [
        ('Compressive', 'Compressive Strength'),
        ('Slump', 'Slump'),
        ('Tensile', 'Tensile Strength'),
        ('Sieve', 'Sieve Analysis'),
        ('WaterAbs', 'Water Absorption'),
    ]
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='material_tests')
    material_type = models.ForeignKey(MaterialType, on_delete=models.CASCADE, related_name='tests')
    sample_id = models.CharField(max_length=100, blank=True)
    test_type = models.CharField(max_length=50, choices=TEST_TYPES)
    test_date = models.DateField()
    performed_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='performed_tests')
    remarks = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.project.name} - {self.material_type.name} - {self.test_type} ({self.sample_id})"

class TestResult(models.Model):
    test = models.ForeignKey(MaterialTest, on_delete=models.CASCADE, related_name='results')
    parameter = models.CharField(max_length=150)  # e.g., '28_day_strength'
    value = models.FloatField()
    unit = models.CharField(max_length=30, default='MPa')
    status = models.CharField(max_length=30, blank=True)  # 'Pass' or 'Fail' - can be computed

    def __str__(self):
        return f"{self.test} - {self.parameter}: {self.value}{self.unit}"

class TestReport(models.Model):
    test = models.ForeignKey(MaterialTest, on_delete=models.CASCADE, related_name='reports')
    file = models.FileField(upload_to='reports/', null=True, blank=True)
    approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

class Notification(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='notifications')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='notifications', null=True, blank=True)
    message = models.TextField()
    read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
