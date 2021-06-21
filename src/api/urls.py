from typing import ValuesView
from django.urls import path
from . import views

urlpatterns = [
    path('courses/', views.CourseList.as_view(), name=views.CourseList.name),
    path('courses/<int:pk>/', views.CourseDetail.as_view(),
         name=views.CourseDetail.name),
    path('course-category/', views.CourseCategoryList.as_view(),
         name=views.CourseCategoryList.name),
    path('course-category/<int:pk>/', views.CourseCategoryDetail.as_view(),
         name=views.CourseCategoryDetail.name)
]
