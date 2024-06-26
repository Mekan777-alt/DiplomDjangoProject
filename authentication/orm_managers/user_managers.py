from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.password_validation import validate_password
from authentication.enum import Groups


class UserManager(BaseUserManager):
    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        if 'role' not in extra_fields:
            extra_fields['role'] = Groups.DECANAT.name

        return self.create_user(email, password, **extra_fields)

    def create_user(self, email, password, role, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address.')

        email = self.normalize_email(email)
        role_value = role.name if isinstance(role, Groups) else role
        user = self.model(email=email, role=role_value, **extra_fields)
        validate_password(password)
        user.set_password(password)
        user.save()

        return user
