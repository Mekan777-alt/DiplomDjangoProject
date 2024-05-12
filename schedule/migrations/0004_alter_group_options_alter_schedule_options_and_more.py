# Generated by Django 4.0 on 2024-05-11 20:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0003_subject_schedule_subject'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='group',
            options={'verbose_name': 'Группы студентов', 'verbose_name_plural': 'Группы студентов'},
        ),
        migrations.AlterModelOptions(
            name='schedule',
            options={'verbose_name': 'Расписание студентов', 'verbose_name_plural': 'Расписание студентов'},
        ),
        migrations.AlterModelOptions(
            name='subject',
            options={'verbose_name': 'Предметы студентов', 'verbose_name_plural': 'Предметы студентов'},
        ),
        migrations.AlterField(
            model_name='group',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Название группы'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.group', verbose_name='Название группы'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='number',
            field=models.IntegerField(verbose_name='Номер пары'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.subject', verbose_name='Название предмета'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='time_from',
            field=models.TimeField(verbose_name='Начало пары'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='time_to',
            field=models.TimeField(verbose_name='Конец пары'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Название предмета'),
        ),
    ]
