from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as UserAdminBase
from apps.users.models import User

@admin.register(User)
class UserAdmin(UserAdminBase):
    pass