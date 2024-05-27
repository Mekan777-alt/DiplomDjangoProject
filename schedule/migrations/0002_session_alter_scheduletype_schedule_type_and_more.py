# Generated by Django 4.0 on 2024-05-27 07:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_number', models.IntegerField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8')], max_length=10, unique=True, verbose_name='Номер сессии')),
            ],
        ),
        migrations.AlterField(
            model_name='scheduletype',
            name='schedule_type',
            field=models.CharField(choices=[('Предмет', 'Предмет'), ('Сессия', 'Сессия')], max_length=10, verbose_name='Тип расписания'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='session_number',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='schedule.session', verbose_name='Номер сессии'),
        ),
    ]
