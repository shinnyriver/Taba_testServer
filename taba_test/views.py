from django.db.models import Max, Min
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
import csv
from django.conf import settings
from pathlib import Path


def append_to_csv(filename, data):
    file_path = Path(settings.BASE_DIR) / "data" / filename
    file_exists = file_path.is_file()

    with open(file_path, mode="a", newline="", encoding="utf-8") as csvfile:
        fieldnames = data.keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()
        writer.writerow(data)


class AccelPressureData(APIView):
    def post(self, request, *args, **kwargs):
        serializer = AccelPressureSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        pressures = Pressure_Accel.objects.all()
        serializer = AccelPressureSerializer(pressures, many=True)
        return Response(serializer.data)


class BreakPressureData(APIView):
    def post(self, request, *args, **kwargs):
        serializer = BreakPressureSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        pressures = Pressure_Break.objects.all()
        serializer = BreakPressureSerializer(pressures, many=True)
        return Response(serializer.data)


class PressureData(APIView):
    def post(self, request, *args, **kwargs):
        serializer = PressureSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        pressures = Pressure.objects.all()
        serializer = PressureSerializer(pressures, many=True)
        return Response(serializer.data)


class SpeedData(APIView):
    def post(self, request, *args, **kwargs):
        serializer = SpeedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        speeds = Speed.objects.all()
        serializer = AccelPressureSerializer(speeds, many=True)
        return Response(serializer.data)


class CalibrationData(APIView):
    def post(self, request, *args, **kwargs):
        serializer = CalibrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        data = Calibration.objects.all()
        serializer = CalibrationSerializer(data, many=True)
        return Response(serializer.data)


class SensorCalibrationData(APIView):
    def get(self, request, sensor_id):
        aggregates = Calibration.objects.filter(sensor_id=sensor_id).aggregate(
            Max("break_value"),
            Min("break_value"),
            Max("accel_value"),
            Min("accel_value"),
        )

        result = {
            "sensor_id": sensor_id,
            "break_max": aggregates["break_value__max"],
            "break_min": aggregates["break_value__min"],
            "accel_max": aggregates["accel_value__max"],
            "accel_min": aggregates["accel_value__min"],
        }

        return Response(result)


class TestsetData(APIView):
    def post(self, request, *args, **kwargs):
        serializer = TestsetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        data = Testset.objects.all()
        serializer = TestsetSerializer(data, many=True)
        return Response(serializer.data)


@api_view(["GET"])
def get_csv(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="Testfile.csv"'

    writer = csv.writer(response)
    writer.writerow(["break_value", "accel_value", "speed", "timestamp"])

    ValueList = (
        Testset.objects.all()
        .values_list("break_value", "accel_value", "speed", "timestamp")
        .order_by("timestamp")
    )
    for values in ValueList:
        writer.writerow(values)
    return response


@api_view(["GET"])
def get_csv_in_local(request):
    file_path = "Testfile.csv"

    with open(file_path, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["break_value", "accel_value", "speed", "timestamp"])

        ValueList = (
            Testset.objects.all()
            .values_list("break_value", "accel_value", "speed", "timestamp")
            .order_by("timestamp")
        )
        for values in ValueList:
            writer.writerow(values)

    return HttpResponse(
        "CSV file has been created successfully.", content_type="text/plain"
    )
