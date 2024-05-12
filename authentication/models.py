from django.db import models
from authentication.enum import Groups
from django.contrib.auth.models import AbstractUser
from authentication.orm_managers.user_managers import UserManager


class User(AbstractUser):
    objects = UserManager()

    email = models.EmailField('Электронная почта', unique=True)
    role = models.CharField('Роль', max_length=50, choices=[(tag.name, tag.value) for tag in Groups],
                            default=Groups.STUDENT.value)

    REQUIRED_FIELDS = ['first_name', 'last_name', 'patronymic']
    USERNAME_FIELD = 'email'

    first_name = models.CharField('Имя', max_length=255)
    last_name = models.CharField('Фамилия', max_length=255)
    patronymic = models.CharField('Отчество', max_length=255)
    username = None

    class Meta:
        verbose_name = 'Пользователи'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f"{self.last_name} {self.first_name[0]} {self.patronymic[0]}"
