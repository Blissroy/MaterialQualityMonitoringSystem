from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200, blank=True)
    client = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class MaterialTest(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tests')
    tester = models.CharField(max_length=150, blank=True)
    date = models.DateField()
    notes = models.TextField(blank=True)

    class Meta:
        abstract = True


class ConcreteTest(MaterialTest):
    mix_design = models.CharField(max_length=200, blank=True)
    slump_mm = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    compressive_strength_mpa = models.DecimalField(max_digits=8, decimal_places=2)
    sample_id = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"ConcreteTest {self.id} - {self.project.name}"


class SteelTest(MaterialTest):
    grade = models.CharField(max_length=100, blank=True)
    yield_strength_mpa = models.DecimalField(max_digits=8, decimal_places=2)
    ultimate_strength_mpa = models.DecimalField(max_digits=8, decimal_places=2)
    elongation_percent = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"SteelTest {self.id} - {self.project.name}"


class AggregateTest(MaterialTest):
    fineness_modulus = models.DecimalField(max_digits=6, decimal_places=3, null=True, blank=True)
    water_absorption_percent = models.DecimalField(max_digits=6, decimal_places=3, null=True, blank=True)
    sieve_results = models.JSONField(null=True, blank=True)  # { "25mm": 0, "20mm": 12.5, ... }

    def __str__(self):
        return f"AggregateTest {self.id} - {self.project.name}"
