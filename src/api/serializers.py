from rest_framework import serializers

from .models import CourseCategory, Course


class CourseCategorySerializer(serializers.HyperlinkedModelSerializer):
    courses = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='course-detail')

    class Meta:
        model = CourseCategory
        fields = ['url', 'pk', 'name', 'courses']


class CourseSerializer(serializers.HyperlinkedModelSerializer):
    category = serializers.SlugRelatedField(
        queryset=CourseCategory.objects.all(), slug_field='name')

    class Meta:
        model = Course
        fields = ['url', 'name', 'category', 'created', 'updated']


class CourseCategoryDetailSerializer(serializers.HyperlinkedModelSerializer):
    courses = CourseSerializer(many=True, read_only=True)

    class Meta:
        model = CourseCategory
        fields = ['url', 'pk', 'name', 'courses']
