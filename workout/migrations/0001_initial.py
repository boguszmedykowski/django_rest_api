# Generated by Django 4.1.7 on 2023-03-04 10:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='trening', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('series', models.IntegerField(default=1)),
                ('reps', models.IntegerField(default=1)),
                ('workout', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workout.workout')),
            ],
        ),
    ]
