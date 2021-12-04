from django.db.models import Max
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from task2_main.models import VoltageSensor, Measurement
from task2_api.serializers import VoltageSensorActualSerializer, MeasurementActualSerializer
#from task2_api.permissions import AdminAuthenticationPermission

class AdminVoltageSensorRecentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that gets ip of sensor.
    """
    queryset= VoltageSensor.objects.all().filter(
        measurement__is_error=False,    
    )
    serializer_class = VoltageSensorActualSerializer

    def get_object(self):
        qs = super().get_queryset()
        id_m= int(filter(id=qs.aggregate(Max('id'))))
        try:
            if id_m:
                obj = Measurement.objects.get(id=id_m)
                return qs.get(measuremet=obj)
        except:
            pass

class AdminMeasurementRecentViewSet(viewsets.ModelViewSet):

    serializer_class = MeasurementActualSerializer
    queryset= Measurement.objects.all().filter(
        is_error=False,  
    ).order_by('id').reverse()[:1]

class MeasurementViewSet(viewsets.ViewSet):
    """
    API endpoint that gets the most recent record.
    """
    def retrieve(self):
        queryset = Measurement.objects.filter(
        is_error=False,  
    ).order_by('id').reverse()
        measurement = get_object_or_404(queryset)
        serializer = MeasurementActualSerializer(measurement)
        return Response(serializer.data) 