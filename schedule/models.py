from django.db import models
from authentication.models import User
from authentication.enum import Groups


class TeacherManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(groups__name=Groups.TEACHER.name)


class Group(models.Model):
    name = models.CharField("Название группы", max_length=100)

    def __str__(self):

        return self.name

    class Meta:

        verbose_name_plural = 'Группы студентов'
        verbose_name = 'Группы студентов'


class Subject(models.Model):
    name = models.CharField("Название предмета", max_length=100)

    def __str__(self):

        return self.name

    class Meta:
        verbose_name_plural = 'Предметы студентов'
        verbose_name = 'Предметы студентов'


class Schedule(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name="Название группы")
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name="Название предмета")
    day_of_week = models.CharField('День недели', max_length=150)
    number = models.IntegerField("Номер пары")
    time_from = models.TimeField("Начало пары")
    time_to = models.TimeField("Конец пары")
    type_of_lesson = models.CharField('Вид занятий', max_length=150)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Преподаватель',
                                limit_choices_to={'role': Groups.TEACHER.name})
    place_of_perfomance = models.CharField('Место проведение', max_length=150)

    def __str__(self):

        return f"{self.type_of_lesson} - {self.subject} - {self.teacher}"

    class Meta:
        verbose_name_plural = 'Расписание студентов'
        verbose_name = 'Расписание студентов'
