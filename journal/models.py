from django.db import models
from authentication.models import User, Group, Groups
from schedule.models import Schedule, Subject


class Grade(models.Model):
    GRADE_TYPES = [
        ('lesson', 'За урок'),
        ('session', 'За сессию'),
    ]

    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='student_grades', verbose_name='Студент',
                                limit_choices_to={'role': Groups.STUDENT.name})
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Преподаватель',
                                limit_choices_to={'role': Groups.TEACHER.name})
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='lesson_grades', verbose_name='Предмет')
    mark = models.IntegerField('Оценка')
    grade_type = models.CharField('Тип оценки', choices=GRADE_TYPES, default='lesson', max_length=10)
    subject_date = models.ForeignKey(Schedule, on_delete=models.CASCADE, verbose_name='Урок или сессия')
    date = models.DateField('Дата', auto_now_add=True)

    class Meta:
        verbose_name = 'Оценка'
        verbose_name_plural = 'Оценки'


