from django.contrib import admin
from .models import User


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'first_name',
                    'last_name', 'is_superuser')
    ordering = ('id',)
    search_fields = ('username',)


admin.site.register(User, UserAdmin)
