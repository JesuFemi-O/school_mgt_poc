from typing import ClassVar
from django.db import models
from django.db.models.base import Model
from auth_app.models import User

# Create your models here.


class CourseCategory(models.Model):
    name = models.CharField(max_length=256)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)

    def __str__(self) -> str:
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=256)
    category = models.ForeignKey(
        CourseCategory, related_name='courses', on_delete=models.CASCADE)
    preview_url = models.URLField(max_length=526, blank=True, null=True)
    description = models.CharField(max_length=1000, blank=True, null=True)
    owner = models.ForeignKey(
        User, related_name='courses', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self) -> str:
        return self.name


class Lecture(models.Model):
    name = models.CharField(max_length=256)
    duration = models.PositiveIntegerField(default=1)
    course = models.ForeignKey(
        Course, related_name='lectures', on_delete=models.CASCADE)
    video = models.URLField(max_length=526, blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self) -> str:
        return self.name


class Rating(models.Model):
    rate = models.DecimalField(max_digits=1, decimal_places=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'course')
        ordering = ('-created',)

    def __str__(self) -> str:
        return self.course.name + "_rating"


class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'course')
        ordering = ('-created',)

    def __str__(self) -> str:
        return self.course.name + "_" + self.user.username
