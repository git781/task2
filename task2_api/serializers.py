from rest_framework import serializers

from task2_main.models import VoltageSensor, Measurement

class VoltageSensorActualSerializer(serializers.ModelSerializer):
    class Meta:
        model = VoltageSensor
        fields = '__all__'

class MeasurementActualSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = '__all__'