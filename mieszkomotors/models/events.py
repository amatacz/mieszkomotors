from django.db import models

from mieszkomotors.models.base import PublicationTracker, RENEWAL_INTERVAL
from mieszkomotors.models.car import *
from mieszkomotors.models.insurance import *


class CarEvent(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    start_date = models.DateTimeField(blank=True)
    end_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.car} {self.car.license_plates}: {self.start_date.strftime("%Y-%m-%d")}'

class InsuranceEvent(models.Model):
    insurance = models.ForeignKey(Insurance, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    start_date = models.DateTimeField(blank=True)
    end_date = models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return f'{self.insurance.car} {self.insurance.car.license_plates}: {self.start_date.strftime("%Y-%m-%d")}'