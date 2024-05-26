from django.db import models
from authentication.models import User, Group, Groups
from schedule.models import Schedule, Subject


class Grade(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='student_grades', verbose_name='Студент',
                                limit_choices_to={'role': Groups.STUDENT.name})
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Преподаватель',
                                limit_choices_to={'role': Groups.TEACHER.name})
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='lesson_grades', verbose_name='Урок')
    mark = models.IntegerField('Оценка')
    subject_date = models.ForeignKey(Schedule, on_delete=models.CASCADE, verbose_name='К какому уроку',
                                     default=None)
    date = models.DateField('Дата', auto_now_add=True)

    class Meta:
        verbose_name = 'Оценка'
        verbose_name_plural = 'Оценки'

    def __str__(self):
        return f"{self.student} - {self.mark}"

