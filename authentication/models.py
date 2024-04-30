from django.db import models
from django.contrib.auth.models import AbstractUser
from authentication.orm_managers.user_managers import UserManager


class User(AbstractUser):
    objects = UserManager()

    email = models.EmailField('Электронная почта', unique=True)

    REQUIRED_FIELDS = ['first_name', 'last_name']
    USERNAME_FIELD = 'email'

    first_name = models.CharField('Имя', max_length=255)
    last_name = models.CharField('Фамилия', max_length=255)

    username = None

    class Meta:
        verbose_name = 'Пользователи'
        verbose_name_plural = 'Пользователи'
