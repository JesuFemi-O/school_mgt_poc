from django.contrib import admin
from .models import CourseCategory, Course, Lecture, Rating, Enrollment
# Register your models here.


class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'updated',)
    ordering = ('-created',)
    search_fields = ('name',)


class CourseCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'updated',)
    ordering = ('-created',)
    search_fields = ('name',)


class LectureAdmin(admin.ModelAdmin):
    list_display = ('name', 'course', 'duration', 'created',)
    ordering = ('-course',)
    search_fields = ('name', 'course')


class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('course', 'user', 'created',)
    ordering = ('-created', '-course')
    search_fields = ('course',)


admin.site.register(Course, CourseAdmin)
admin.site.register(CourseCategory, CourseCategoryAdmin)
admin.site.register(Lecture, LectureAdmin)
admin.site.register(Enrollment, EnrollmentAdmin)
