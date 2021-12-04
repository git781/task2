from django.urls import path, include

from rest_framework import routers

from task2_api import views

app_name = 'task2_api'

router = routers.DefaultRouter()
router.register(r'sensor/create/', views.AdminVoltageSensorRecentViewSet)
router.register(r'measurement/create/', views.AdminMeasurementRecentViewSet)

urlpatterns =[ 
    path('', include(router.urls)), 
    path('/recent', views.MeasurementViewSet.as_view({'get':'retrieve'}, name="recent")),
]