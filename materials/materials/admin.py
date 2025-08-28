from django.contrib import admin
from .models import Project, ConcreteTest, SteelTest, AggregateTest

admin.site.register(Project)
admin.site.register(ConcreteTest)
admin.site.register(SteelTest)
admin.site.register(AggregateTest)
