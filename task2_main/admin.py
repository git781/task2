from django.contrib import admin
from task2_main.models import VoltageSensor, Measurement

@admin.register(VoltageSensor)
class VoltageSensorAdmin(admin.ModelAdmin):
    list_display=('ip',)

@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    list_display=('time_stamp','current_voltage','is_error')
    list_filter=('is_error',)
