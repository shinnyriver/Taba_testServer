from rest_framework import serializers
from .models import *


class AccelPressureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pressure_Accel
        fields = ["id", "value", "timestamp"]


class BreakPressureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pressure_Break
        fields = ["id", "value", "timestamp"]


class PressureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pressure
        fields = ["id", "break_value", "accel_value", "timestamp"]


class SpeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Speed
        fields = ["id", "value", "timestamp"]
