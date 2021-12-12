from django.urls import path, include

from rest_framework import routers

from task2_api import views

app_name = 'task2_api'

router = routers.DefaultRouter()
router.register(r'recent/sensor/', views.AdminVoltageSensorRecentViewSet)
router.register(r'recent/measurement/', views.AdminMeasurementRecentViewSet)

urlpatterns =[ 
    path('', include(router.urls)), 
    #path('model/predict/<name>/dumb_model/', views.AdminMeasurementViewSet.as_view({'get':'retrieve'}, name='datetime_valid'), name='dumb_model'),
]