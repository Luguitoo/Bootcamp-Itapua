

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser
# crear administrador de usuarios personalizado
class UserAdmin(BaseUserAdmin):
    # establecer columnas que se veran en la tabla de usuarios
    list_display= (
        "username",
        "email",
        "is_active",
        "is_staff",
        "is_superuser",
    )
    # establecer campos y orden de formulario para agregar usuario
    add_fieldsets= (
        (None, {
        'fields': (
        'username',
        'email',
        'password1',
        'password2',
        )}
        ),
    )
    # establecer campos y orden de formulario para editar usuario
    fieldsets= (
        (None, {'fields': (
        'username',
        'email',
        'age',
        'password'
    )}),
    ('Permissions', {'fields': (
        'is_active',
        'is_staff',
        'is_superuser',
        'groups',
        'user_permissions'
        )}),
    )
    # establecer cmpos de busqueda del buscador de usuarios
    search_fields= ('username', 'email')
    
admin.site.register(CustomUser, UserAdmin)
