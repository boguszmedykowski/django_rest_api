# Generated by Django 4.1.7 on 2023-03-05 19:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('workout', '0002_workout_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workout',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
