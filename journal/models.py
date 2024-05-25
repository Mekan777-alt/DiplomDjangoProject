from django.db import models
from authentication.models import User, Group, Groups
from schedule.models import Schedule


class Grade(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='student_grades', verbose_name='Студент',
                                limit_choices_to={'role': Groups.STUDENT.name})
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Преподаватель',
                                limit_choices_to={'role': Groups.TEACHER.name})
    lesson = models.ForeignKey(Schedule, on_delete=models.CASCADE, related_name='lesson_grades', verbose_name='Урок')
    score = models.IntegerField('Оценка')
    date = models.DateField('Дата', auto_now_add=True)

    class Meta:
        verbose_name = 'Оценка'
        verbose_name_plural = 'Оценки'

    def __str__(self):
        return f"{self.student} - {self.score}"


class TeachingAssignment(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Преподаватель',
                                limit_choices_to={'role': Groups.TEACHER.name})
    subject = models.ForeignKey('schedule.Subject', on_delete=models.CASCADE, verbose_name='Предмет')
    group = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name='Группа')

    class Meta:
        verbose_name = 'Преподователи'
        verbose_name_plural = 'Преподователи'

    def __str__(self):
        return f"{self.group} группа: {self.subject} - {self.teacher}"
