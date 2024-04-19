from django.db import models


class Schedule(models.Model):
    day_of_week = models.CharField('День недели', max_length=150)
    number = models.IntegerField()
    time_from = models.TimeField()
    time_to = models.TimeField()
    name_of_discipline = models.CharField('Наименование дисциплины', max_length=150)
    type_of_lesson = models.CharField('Вид занятий', max_length=150)
    teacher = models.CharField('Преподаватель', max_length=150)
    place_of_perfomance = models.CharField('Место проведение', max_length=150)

    def __str__(self):

        return f"{self.type_of_lesson} - {self.name_of_discipline} - {self.teacher}"
