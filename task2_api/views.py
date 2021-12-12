from django.db.models import Max
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.dectoators import action
from rest_framework.response import Response

from task2_main.models import VoltageSensor, Measurement, ValidatedMeasurement
from task2_api.serializers import VoltageSensorActualSerializer, MeasurementActualSerializer, ValidatedMeasurementSerializer
from task2_api.utils import estimate_coef
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

class AdminMeasurementViewSet(viewsets.ModelViewSet):
    serializer_class = ValidatedMeasurementSerializer
    queryset= ValidatedMeasurement.objects.all()

    @action(detail=True, methods=['get'])
    def dumb_model(self, request):
        datetime_local = self.kwargd['name']
        qs=super().get_queryset()
        #In summary, if y = mx + b, then m is the slope and b is the y-intercept (i.e., the value of y when x = 0). 
        #b_0 and b_1 are regression coefficients and represent y-intercept and slope of regression line respectively.


    