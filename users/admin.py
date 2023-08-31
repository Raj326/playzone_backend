from django.contrib import admin
from django.contrib.auth import get_user_model

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser


# Register your models here.
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ("email", "name", "is_active")
