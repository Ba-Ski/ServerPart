import datetime

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone



class User(models.Model):
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return self.login


class BatteryMode(models.Model):
    mode_text = models.CharField(max_length=10)

    def __str__(self):
        return self.mode_text


class DeviceState(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    temperature = models.IntegerField(default=0)
    temperature_limit = models.IntegerField(default=0)
    battery_mode = models.ForeignKey(BatteryMode, on_delete=models.CASCADE)
    refresh_date = models.DateTimeField()

    def __str__(self):
        return self.user.__str__() + " " + str(self.temperature) + \
                " " + str(self.temperature_limit) + \
                " " + self.battery_mode.__str__()
