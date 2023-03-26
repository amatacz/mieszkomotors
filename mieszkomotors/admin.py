from django.contrib import admin
from mieszkomotors.models.car import CarEnterpriseOwner, CarIndividualOwner, CarSelfEmploedOwner, Car
from mieszkomotors.models.insurance import Insurance
from mieszkomotors.models.owner import IndividualOwner,IndividualOwnerAttachment, IndividualOwnerNotes, EnterpriseOwner
from mieszkomotors.models.owner import SelfEmployedOwnerAttachment, SelfEmployedOwnerNotes, SelfEmployedOwner



admin.site.register(Car)
admin.site.register(Insurance)
admin.site.register(CarIndividualOwner)
admin.site.register(CarSelfEmploedOwner)
admin.site.register(CarEnterpriseOwner)
admin.site.register(IndividualOwner)
admin.site.register(IndividualOwnerAttachment)
admin.site.register(IndividualOwnerNotes)
admin.site.register(EnterpriseOwner)
admin.site.register(SelfEmployedOwner)
admin.site.register(SelfEmployedOwnerAttachment)
admin.site.register(SelfEmployedOwnerNotes)