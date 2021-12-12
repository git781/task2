from rest_framework import serializers

from task2_main.models import VoltageSensor, Measurement, ValidatedMeasurement

class VoltageSensorActualSerializer(serializers.ModelSerializer):
    class Meta:
        model = VoltageSensor
        fields = '__all__'

class MeasurementActualSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = '__all__'

class ValidatedMeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = ValidatedMeasurement
        fields = '__all__'