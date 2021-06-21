from django.db import models


class UserTypes(models.TextChoices):
    INSTRUCTOR = "INSTRUCTOR", "Instructor"
    STUDENT = "STUDENT", "Student"
    SYSTEM_ADMIN = "SYSTEM ADMIN", "System Admin"


default_role = UserTypes.STUDENT
