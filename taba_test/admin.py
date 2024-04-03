from django.contrib import admin
from .models import Pressure_Accel, Pressure_Break, Speed


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
