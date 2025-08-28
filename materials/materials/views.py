from rest_framework import viewsets
from .models import Project, ConcreteTest, SteelTest, AggregateTest
from .serializers import (
    ProjectSerializer, ConcreteTestSerializer,
    SteelTestSerializer, AggregateTestSerializer
)

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ConcreteTestViewSet(viewsets.ModelViewSet):
    queryset = ConcreteTest.objects.all()
    serializer_class = ConcreteTestSerializer

class SteelTestViewSet(viewsets.ModelViewSet):
    queryset = SteelTest.objects.all()
    serializer_class = SteelTestSerializer

class AggregateTestViewSet(viewsets.ModelViewSet):
    queryset = AggregateTest.objects.all()
    serializer_class = AggregateTestSerializer

