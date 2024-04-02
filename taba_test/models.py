from django.db import models


class Pressure_Accel(models.Model):
    value = models.FloatField(
        help_text="Acclerator Pressure value in Pa"
    )  # 파스칼 단위의 입력 값
    timestamp = models.DateTimeField(
        auto_now_add=True, help_text="The time data was received"
    )  # 입력 받은 시간

    def __str__(self):
        return f"Accel Pressure {self.value} Pa at {self.timestamp}"


class Pressure_Break(models.Model):
    value = models.FloatField(help_text="Break Pressure value in Pa")  # 파스칼 단위의 입력 값
    timestamp = models.DateTimeField(
        auto_now_add=True, help_text="The time data was received"
    )  # 입력 받은 시간

    def __str__(self):
        return f"Break Pressure {self.value} Pa at {self.timestamp}"


class Speed(models.Model):
    value = models.FloatField(help_text="Speed value in Km/h")
    timestamp = models.DateTimeField(
        auto_now_add=True, help_text="The time data was received"
    )

    def __str__(self):
        return f"Speed {self.value} km/h at {self.timestamp}"
