from django.contrib.auth.models import User 
from django.db import models
from django.utils import formats
from django.utils.timezone import localtime

class VoltageSensor(models.Model):
    ip=models.CharField(max_length=15, null=True, blank=True, verbose_name='IP')

class Measurement(models.Model):
    sensor=models.ForeignKey(VoltageSensor, on_delete=models.CASCADE, verbose_name='VoltageSensor')
    time_stamp=models.DateTimeField(verbose_name='Date and time of the measurement:')
    current_voltage=models.DecimalField(max_digits=8, decimal_places=2, default=20, verbose_name='Voltage measurement value:')
    is_error=models.BooleanField(default=False, verbose_name='Activeness')
    @property
    def get_created_at_time(self):
        return formats.date_format(localtime(self.time_stamp), "DATETIME_FORMAT")