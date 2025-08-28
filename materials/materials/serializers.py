from rest_framework import serializers
from .models import Project, ConcreteTest, SteelTest, AggregateTest

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class ConcreteTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConcreteTest
        fields = '__all__'

class SteelTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = SteelTest
        fields = '__all__'

class AggregateTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = AggregateTest
        fields = '__all__'
