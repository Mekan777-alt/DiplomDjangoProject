# Generated by Django 4.0 on 2024-05-26 16:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0013_alter_schedule_place_of_perfomance_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='schedule',
            old_name='typy_schedule',
            new_name='type_schedule',
        ),
    ]