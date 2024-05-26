# Generated by Django 4.0 on 2024-05-26 11:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0002_subject_alter_schedule_options_and_more'),
        ('authentication', '0001_initial'),
        ('journal', '0008_rename_score_grade_mark'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeachingAssignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.group', verbose_name='Группа')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.subject', verbose_name='Предмет')),
                ('teacher', models.ForeignKey(limit_choices_to={'role': 'TEACHER'}, on_delete=django.db.models.deletion.CASCADE, to='authentication.user', verbose_name='Преподаватель')),
            ],
            options={
                'verbose_name': 'Преподователи',
                'verbose_name_plural': 'Преподователи',
            },
        ),
    ]
