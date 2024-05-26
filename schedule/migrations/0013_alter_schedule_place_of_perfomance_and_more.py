# Generated by Django 4.0 on 2024-05-26 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0012_alter_schedule_number_alter_schedule_time_from'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='place_of_perfomance',
            field=models.CharField(max_length=150, null=True, verbose_name='Место проведение'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='time_to',
            field=models.TimeField(null=True, verbose_name='Конец пары'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='type_of_lesson',
            field=models.CharField(max_length=150, null=True, verbose_name='Вид занятий'),
        ),
    ]
