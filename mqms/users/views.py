from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import CustomUser
from .serializers import UserSerializer
from rest_framework.permissions import IsAdminUser

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]
from django.http import HttpResponse

def users_home(request):
    return HttpResponse("Users API Home 🚧")
