from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from .utils import UserTypes, default_role
# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if username is None:
            raise TypeError("users should have a username")

        if email is None:
            raise TypeError("Users Should have an email")

        user = self.model(username=username, email=self.normalize_email(email))

        user.set_password(password)

        user.save()

        return user

    def create_superuser(self, username, email, password):
        if password is None:
            raise TypeError("Password should not be none")

        user = self.create_user(username, email, password)

        user.is_superuser = True
        user.is_staff = True
        user.role = UserTypes.SYSTEM_ADMIN

        user.save()

        return user


AUTH_PROVIDERS = {'google': 'google', 'email': 'email'}


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True, db_index=True)
    email = models.CharField(max_length=255, unique=True, db_index=True)
    first_name = models.CharField(max_length=400)
    last_name = models.CharField(max_length=400)
    role = models.CharField(_("UserTypes"), max_length=58,
                            choices=UserTypes.choices, default=default_role)
    display_picture = models.URLField(max_length=526, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    auth_provider = models.CharField(
        max_length=255, blank=False, null=False, default=AUTH_PROVIDERS.get('email'))

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.email
