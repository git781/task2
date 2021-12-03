from django.db import models

class VoltageSensor(models.Model):
    time_stamp=models.DateTimeField(verbose_name='Date and time of the measurement:')
    current_voltage=models.DecimalField(max_digits=8, decimal_places=2, default=20, verbose_name='Voltage measurement value:')
    is_error=models.BooleanField(default=False, verbose_name='Activeness')
    ip=models.CharField(max_length=15, null=True, blank=True, verbose_name='IP')

