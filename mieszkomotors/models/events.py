from django.db import models

from mieszkomotors.models.base import PublicationTracker, RENEWAL_INTERVAL
from mieszkomotors.models.car import *
from mieszkomotors.models.insurance import *


class CarEvent(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200, default="Default description")
    start = models.DateField(blank=True)
    end = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.car}: {self.start.strftime("%Y-%m-%d")}'

class InsuranceEvent(models.Model):
    insurance = models.ForeignKey(Insurance, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200, default="Default description")
    start = models.DateField(blank=True)
    end = models.DateField(null=True,blank=True)

    def __str__(self):
        return f'{self.insurance.car}: {self.start.strftime("%Y-%m-%d")}'