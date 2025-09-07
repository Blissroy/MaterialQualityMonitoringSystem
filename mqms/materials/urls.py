from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    MaterialTypeViewSet,
    MaterialTestViewSet,
    TestResultViewSet,
    TestReportViewSet,
    materials_home,
    upload_tests_file
)

router = DefaultRouter()
router.register(r'types', MaterialTypeViewSet, basename='materialtype')
router.register(r'tests', MaterialTestViewSet, basename='materialtest')
router.register(r'results', TestResultViewSet, basename='testresult')
router.register(r'reports', TestReportViewSet, basename='testreport')

urlpatterns = [
    path('', materials_home, name="materials-home"),
    path('upload/', upload_tests_file, name="upload-tests"),
    path('', include(router.urls)),
]


