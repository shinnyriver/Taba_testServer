from django.urls import path

from .views import (
    AccelPressureData,
    BreakPressureData,
    CalibrationData,
    get_csv_in_local,
    SensorCalibrationData,
    SpeedData,
    PressureData,
    TestsetData,
    get_csv,
)

urlpatterns = [
    path("accelpressure/", AccelPressureData.as_view()),
    path("breakpressure/", BreakPressureData.as_view()),
    path("speed/", SpeedData.as_view()),
    path("pressure/", PressureData.as_view()),
    path(
        "calibration/sensor/<int:sensor_id>/",
        SensorCalibrationData.as_view(),
        name="sensor-calibration-data",
    ),
    path("calibration/", CalibrationData.as_view()),
    path("testdata/", TestsetData.as_view()),
    path("testdata/getcsv/", get_csv, name="get-csv"),
    path("testdata/getcsvinlocal/", get_csv_in_local, name="get-csv-in-local"),
]
