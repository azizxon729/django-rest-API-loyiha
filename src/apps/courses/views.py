from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Course
from .serializers import CourseSerializer


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    search_fields = [
        'title',
        'teacher_name',
        'duration',
        'level',
    ]

    ordering_fields = [
        'id',
        'title',
        'teacher_name',
        'price',
        'created_at',
    ]

    ordering = ['-created_at']