from django.db import models

class VoltageSensor(models.Model):
    ip=models.CharField(max_length=15, null=True, blank=True, verbose_name='IP')

class Measurement(models.Model):
    sensor=models.ForeignKey(VoltageSensor, on_delete=models.CASCADE, verbose_name='VoltageSensor')
    current_voltage=models.DecimalField(max_digits=8, decimal_places=2, default=20, verbose_name='Voltage measurement value:')
    is_error=models.BooleanField(default=False, verbose_name='Activeness')

class ValidatedMeasurement(models.Model):
    sensor=models.ForeignKey(VoltageSensor, on_delete=models.CASCADE, verbose_name='VoltageSensor')
    datetime_valid=models.DateTimeField(verbose_name='Date and time of the measurement:')
    current_voltage=models.DecimalField(max_digits=8, decimal_places=2, default=20, verbose_name='Voltage measurement value:')
    #for endpoint with ML in the future 

class InvalidMeasurement(models.Model):
    current_voltage=models.DecimalField(max_digits=8, decimal_places=2, default=20, verbose_name='Voltage measurement value:')
    is_error=models.BooleanField(default=False, verbose_name='Activeness')
    datetime_valid=models.DateTimeField(verbose_name='Date and time of the measurement:')
    email_sent=models.BooleanField(default=False, verbose_name='Email was sent')