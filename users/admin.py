from django.contrib import admin
from django.contrib.auth import admin as auth_admin

from .forms import UserCreationForm, UserChangeForm
from .models import User

class UserAdmin(auth_admin.UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = ["email", "username",]

admin.site.register(User, UserAdmin)

