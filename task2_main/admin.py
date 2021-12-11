from django.contrib import admin
from task2_main.models import VoltageSensor, Measurement, InvalidMeasurement, ValidatedMeasurement

@admin.register(VoltageSensor)
class VoltageSensorAdmin(admin.ModelAdmin):
    list_display=('ip',)

@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    list_display=('current_voltage','is_error')
    list_filter=('is_error',)

@admin.register(ValidatedMeasurement)
class ValidatedMeasurementAdmin(admin.ModelAdmin):
    list_display=('current_voltage', 'sensor')
    #TODO: 'time_in_poland',

@admin.register(InvalidMeasurement)
class InvalidMeasurementAdmin(admin.ModelAdmin):
    list_display=('current_voltage', 'time_where_sensor', 'email_sent')
    #TODO: 'sensor','time_in_poland', 
