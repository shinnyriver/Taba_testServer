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

    with open(file_path, mode="a", newline="") as csvfile:
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
            append_to_csv("AccelPressureData.csv", serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BreakPressureData(APIView):
    def post(self, request, *args, **kwargs):
        serializer = BreakPressureSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            append_to_csv("BreakPressureData.csv", serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SpeedData(APIView):
    def post(self, request, *args, **kwargs):
        serializer = SpeedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            append_to_csv("SpeedData.csv", serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
