from django.contrib import admin
from authentication.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import messages


class UserAdmin(BaseUserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'patronymic', 'is_staff', 'is_superuser', 'role')
    list_filter = ('is_staff', 'is_superuser', 'role')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'patronymic', 'role')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'first_name', 'last_name', 'patronymic', 'role',
                       'is_staff', 'is_superuser',
                       'date_joined'),
        }),
    )
    ordering = ('email',)

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.role = form.cleaned_data['role']
            obj.set_password(form.cleaned_data['password1'])

        obj.save()

        if change:
            self.message_user(request, 'Пользователь успешно обновлен.')
        else:
            self.message_user(request, 'Пользователь успешно создан.')


admin.site.register(User, UserAdmin)
