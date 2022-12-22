from django.contrib import admin
from authentication.models import Usuario
from django.contrib.auth import admin as auth_admin
from authentication.forms import UserCreationForm, UserChangeForm

# Register your models here.
@admin.register(Usuario)
class UsuarioAdmin(auth_admin.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    model = Usuario

