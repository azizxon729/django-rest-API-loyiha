from rest_framework import serializers
from .models import Course


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = [
            'id',
            'title',
            'teacher_name',
            'price',
            'duration',
            'level',
            'created_at',
        ]
        read_only_fields = ['id', 'created_at']