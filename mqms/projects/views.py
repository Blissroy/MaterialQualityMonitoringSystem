from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Project
from .serializers import ProjectSerializer
from rest_framework.permissions import IsAuthenticated

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]
from django.http import HttpResponse

def index(request):
    return HttpResponse("Projects API Home 🚧")
