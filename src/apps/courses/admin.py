from django.contrib import admin
from .models import Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'teacher_name',
        'price',
        'duration',
        'level',
        'created_at',
    ]

    search_fields = [
        'title',
        'teacher_name',
        'level',
    ]

    list_filter = [
        'level',
        'created_at',
    ]