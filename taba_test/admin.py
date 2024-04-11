from django.contrib import admin
from .models import Pressure, Pressure_Accel, Pressure_Break, Speed, Testset


@admin.register(Pressure_Accel)
class Pressure_AccelAdmin(admin.ModelAdmin):
    list_display = ("value", "timestamp")
    list_filter = ("timestamp",)
    search_fields = ("value", "timestamp")


@admin.register(Pressure_Break)
class Pressure_BreakAdmin(admin.ModelAdmin):
    list_display = ("value", "timestamp")
    list_filter = ("timestamp",)
    search_fields = ("value", "timestamp")


@admin.register(Speed)
class SpeedAdmin(admin.ModelAdmin):
    list_display = ("value", "timestamp")
    list_filter = ("timestamp",)
    search_fields = ("value", "timestamp")


@admin.register(Pressure)
class PressureAdmin(admin.ModelAdmin):
    list_display = ("break_value", "accel_value", "timestamp")
    list_filter = ("timestamp",)
    search_fields = ("break_value", "accel_value", "timestamp")


@admin.register(Testset)
class TestsetAdmin(admin.ModelAdmin):
    list_display = ("break_value", "accel_value", "speed", "timestamp")
    list_filter = ("timestamp",)
    search_fields = ("break_value", "accel_value", "speed", "timestamp")
