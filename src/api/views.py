from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .models import Course, CourseCategory
from .serializers import CourseSerializer, CourseCategorySerializer, CourseCategoryDetailSerializer
# Create your views here.


class CourseCategoryList(generics.ListCreateAPIView):
    queryset = CourseCategory.objects.all()
    serializer_class = CourseCategoryDetailSerializer
    name = 'coursecategory-list'


class CourseCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CourseCategory.objects.all()
    serializer_class = CourseCategoryDetailSerializer
    name = 'coursecategory-detail'


class CourseList(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    name = 'course-list'


class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    name = 'course-detail'
