from django.contrib import admin
from . import models


admin.site.register(models.Owner)
admin.site.register(models.Car)
admin.site.register(models.Insurance)
admin.site.register(models.CarEvent)
admin.site.register(models.InsuranceEvent)