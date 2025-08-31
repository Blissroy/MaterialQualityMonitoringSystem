from rest_framework import serializers
from .models import MaterialType, MaterialTest, TestResult, TestReport, Notification
from projects.serializers import ProjectSerializer
from users.serializers import UserSerializer

class MaterialTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaterialType
        fields = '__all__'

class TestResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestResult
        fields = '__all__'

class MaterialTestSerializer(serializers.ModelSerializer):
    results = TestResultSerializer(many=True, read_only=True)
    class Meta:
        model = MaterialTest
        fields = '__all__'

class TestReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestReport
        fields = '__all__'

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'

