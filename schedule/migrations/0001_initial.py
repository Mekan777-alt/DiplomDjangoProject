# Generated by Django 4.0 on 2024-04-19 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_of_week', models.CharField(max_length=150, verbose_name='День недели')),
                ('number', models.IntegerField()),
                ('time_from', models.TimeField()),
                ('time_to', models.TimeField()),
                ('name_of_discipline', models.CharField(max_length=150, verbose_name='Наименование дисциплины')),
                ('type_of_lesson', models.CharField(max_length=150, verbose_name='Вид занятий')),
                ('teacher', models.CharField(max_length=150, verbose_name='Преподаватель')),
                ('place_of_perfomance', models.CharField(max_length=150, verbose_name='Место проведение')),
            ],
        ),
    ]