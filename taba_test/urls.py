from django.urls import path
from .views import AccelPressureData, BreakPressureData, SensorCalibrationData, SpeedData, PressureData

urlpatterns = [
    path("accelpressure/", AccelPressureData.as_view()),
    path("breakpressure/", BreakPressureData.as_view()),
    path("speed/", SpeedData.as_view()),
    path("pressure/", PressureData.as_view()),
    path('calibration/sensor/<int:sensor_id>/', SensorCalibrationData.as_view(), name='sensor-calibration-data'),
]
