from django.contrib import admin
from .forms import UserChangeForm , UserCreationForm
from .models import Account
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

# Register your models here.
class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email','username', 'email_verified', 'superuser' , 'admin')
    list_filter = ('admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password', 'username')}),
        ('Permissions', {'fields': ('admin', 'staff' , 'email_verified' , 'superuser')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username','email_verified', 'password1', 'password2'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(Account, UserAdmin)
admin.site.unregister(Group)