# Generated by Django 3.2.4 on 2021-06-27 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Routine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordinal', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Set',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reps', models.IntegerField()),
                ('seconds_on', models.IntegerField(help_text='Time working out.')),
                ('seconds_off', models.IntegerField(help_text='Time resting between sets.')),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fitness.exercise')),
            ],
        ),
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sets', models.ManyToManyField(through='fitness.Routine', to='fitness.Set', verbose_name='list of sets')),
            ],
        ),
        migrations.AddField(
            model_name='routine',
            name='set',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fitness.set'),
        ),
        migrations.AddField(
            model_name='routine',
            name='workout',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fitness.workout'),
        ),
    ]
