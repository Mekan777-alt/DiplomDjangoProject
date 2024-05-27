from django.utils import timezone
from django.db import models
from authentication.models import User, Group
from authentication.enum import Groups


class TeacherManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(groups__name=Groups.TEACHER.name)

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
    DAYS_OF_WEEK = [
        ('monday', 'Понедельник'),
        ('tuesday', 'Вторник'),
        ('wednesday', 'Среда'),
        ('thursday', 'Четверг'),
        ('friday', 'Пятница'),
        ('saturday', 'Суббота')
    ]
    group = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name="Название группы", default=None)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name="Название предмета", default=None)
    day_of_week = models.CharField('День недели', choices=DAYS_OF_WEEK, max_length=150)
    date = models.DateField(default=timezone.now)
    number = models.IntegerField("Номер пары", null=True)
    time_from = models.TimeField("Начало пары", null=True)
    time_to = models.TimeField("Конец пары", null=True)
    type_of_lesson = models.CharField('Вид занятий', max_length=150, null=True)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Преподаватель',
                                limit_choices_to={'role': Groups.TEACHER.name})
    place_of_perfomance = models.CharField('Место проведение', max_length=150, null=True)
    type_schedule = models.ForeignKey('schedule.ScheduleType', on_delete=models.CASCADE,
                                      verbose_name='Вид рассписания')
    session_number = models.ForeignKey('schedule.Session', on_delete=models.CASCADE, verbose_name='Номер сессии',
                                       default=None)

    def __str__(self):
        return f"{self.type_of_lesson} - {self.subject} - {self.teacher}"

    class Meta:
        verbose_name_plural = 'Расписание студентов'
        verbose_name = 'Расписание студентов'


class ScheduleType(models.Model):
    LESSON = 'Предмет'
    SESSION = 'Сессия'
    TYPE_CHOICES = [
        (LESSON, 'Предмет'),
        (SESSION, 'Сессия'),
    ]
    schedule_type = models.CharField('Тип расписания', max_length=10, choices=TYPE_CHOICES)

    class Meta:
        verbose_name_plural = 'Типы расписания'
        verbose_name = 'Тип расписания'

    def __str__(self):
        return self.schedule_type


class Session(models.Model):
    TYPE_CHOICES = [
        (1, 'Первый семестр'),
        (2, 'Второй семестр'),
        (3, 'Третий семестр'),
        (4, 'Четвертый семестр'),
        (5, 'Пятый семестр'),
        (6, 'Шестой семестр'),
        (7, 'Седьмой семестр'),
        (8, 'Восьмой семестр')
    ]

    session_number = models.IntegerField('Номер сессии', choices=TYPE_CHOICES, max_length=10, unique=True)

    def __str__(self):
        return f"{self.session_number} - семестр"

    class Meta:
        verbose_name_plural = 'Сессия'
        verbose_name = 'Сессия'

