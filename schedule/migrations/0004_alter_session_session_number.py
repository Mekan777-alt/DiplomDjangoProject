# Generated by Django 4.0 on 2024-05-27 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0003_alter_session_options_alter_session_session_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='session_number',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8')], max_length=10, unique=True, verbose_name='Номер сессии'),
        ),
    ]
