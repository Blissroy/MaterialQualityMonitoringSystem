from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from rest_framework import routers
from users.views import UserViewSet
from projects.views import ProjectViewSet
from materials.views import (
    MaterialTypeViewSet,
    MaterialTestViewSet,
    TestResultViewSet,
    TestReportViewSet,
)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


# Default homepage view
def home(request):
    return HttpResponse("Welcome to MQMS Backend API 🚀")


# DRF router for viewsets
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'material-types', MaterialTypeViewSet)
router.register(r'material-tests', MaterialTestViewSet)
router.register(r'test-results', TestResultViewSet)
router.register(r'test-reports', TestReportViewSet)


urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),

    # JWT authentication
    path('api/auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Routers
    path('api/', include(router.urls)),

    # App-specific urls
    path('materials/', include('materials.urls')),
    path('projects/', include('projects.urls')),
    path('users/', include('users.urls')),
]

