# Generated by Django 3.0.14 on 2021-12-03 23:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('task2_main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='voltagesensor',
            name='current_voltage',
        ),
        migrations.RemoveField(
            model_name='voltagesensor',
            name='is_error',
        ),
        migrations.RemoveField(
            model_name='voltagesensor',
            name='time_stamp',
        ),
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_stamp', models.DateTimeField(verbose_name='Date and time of the measurement:')),
                ('current_voltage', models.DecimalField(decimal_places=2, default=20, max_digits=8, verbose_name='Voltage measurement value:')),
                ('is_error', models.BooleanField(default=False, verbose_name='Activeness')),
                ('sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task2_main.VoltageSensor', verbose_name='VoltageSensor')),
            ],
        ),
    ]
