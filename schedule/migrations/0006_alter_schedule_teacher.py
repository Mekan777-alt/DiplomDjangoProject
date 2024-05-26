# Generated by Django 4.0 on 2024-05-26 13:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_teachingassignment'),
        ('schedule', '0005_alter_sessionschedule_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.teachingassignment', verbose_name='Преподаватель'),
        ),
    ]