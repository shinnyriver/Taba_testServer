from django.urls import path
from .views import AccelPressureData, BreakPressureData, SpeedData, PressureData

urlpatterns = [
    path("accelpressure/", AccelPressureData.as_view()),
    path("breakpressure/", BreakPressureData.as_view()),
    path("speed/", SpeedData.as_view()),
    path("pressure/", PressureData.as_view()),
]
