from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import MaterialType, MaterialTest, TestResult, TestReport, Notification
from .serializers import MaterialTypeSerializer, MaterialTestSerializer, TestResultSerializer, TestReportSerializer, NotificationSerializer
from .permissions import IsTechnicianOrAdminWrite, IsAdminOrReadOnly
from rest_framework.permissions import IsAuthenticated

class MaterialTypeViewSet(viewsets.ModelViewSet):
    queryset = MaterialType.objects.all()
    serializer_class = MaterialTypeSerializer
    permission_classes = [IsAdminOrReadOnly]

class MaterialTestViewSet(viewsets.ModelViewSet):
    queryset = MaterialTest.objects.select_related('project','material_type','performed_by').all()
    serializer_class = MaterialTestSerializer
    permission_classes = [IsAuthenticated, IsTechnicianOrAdminWrite]
    filter_backends = [filters.SearchFilter]
    search_fields = ['sample_id','test_type','project__name']

    @action(detail=True, methods=['post'])
    def add_result(self, request, pk=None):
        test = self.get_object()
        serializer = TestResultSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(test=test)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TestResultViewSet(viewsets.ModelViewSet):
    queryset = TestResult.objects.select_related('test').all()
    serializer_class = TestResultSerializer
    permission_classes = [IsAuthenticated]

class TestReportViewSet(viewsets.ModelViewSet):
    queryset = TestReport.objects.select_related('test').all()
    serializer_class = TestReportSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
import pandas as pd
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def upload_tests_file(request):
    file = request.FILES.get('file')
    if not file:
        return Response({"error":"No file"}, status=400)
    if file.name.endswith('.xlsx'):
        df = pd.read_excel(file)
    else:
        df = pd.read_csv(file)
    # expect columns: project, material_type, sample_id, test_type, test_date, parameter, value, unit
    created = 0
    for idx, row in df.iterrows():
        project = Project.objects.get(id=int(row['project']))
        material_type = MaterialType.objects.get(id=int(row['material_type']))
        test = MaterialTest.objects.create(
            project=project, material_type=material_type, sample_id=str(row.get('sample_id','')),
            test_type=row.get('test_type','Compressive'), test_date=row.get('test_date'), performed_by=request.user
        )
        TestResult.objects.create(test=test, parameter=row.get('parameter','value'), value=row.get('value',0), unit=row.get('unit','MPa'))
        created += 1
    return Response({"created":created})
from django.http import HttpResponse

def materials_home(request):
    return HttpResponse("Materials API Home 🧱")

