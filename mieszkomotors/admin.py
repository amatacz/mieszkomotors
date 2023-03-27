from django.contrib import admin
from mieszkomotors.models.car import CarEnterpriseOwner, CarIndividualOwner, CarSelfEmployedOwner, Car
from mieszkomotors.models.insurance import Insurance
from mieszkomotors.models.owner import IndividualOwner,IndividualOwnerAttachment, IndividualOwnerNotes
from mieszkomotors.models.owner import EnterpriseOwner, EnterpriseOwnerAttachment, EnterpriseOwnerNotes
from mieszkomotors.models.owner import SelfEmployedOwnerAttachment, SelfEmployedOwnerNotes, SelfEmployedOwner
from mieszkomotors.models.events import CarEvent, InsuranceEvent



admin.site.register(Car)
admin.site.register(Insurance)
admin.site.register(CarIndividualOwner)
admin.site.register(CarSelfEmployedOwner)
admin.site.register(CarEnterpriseOwner)
admin.site.register(IndividualOwner)
admin.site.register(IndividualOwnerAttachment)
admin.site.register(IndividualOwnerNotes)
admin.site.register(EnterpriseOwner)
admin.site.register(EnterpriseOwnerNotes)
admin.site.register(EnterpriseOwnerAttachment)
admin.site.register(SelfEmployedOwner)
admin.site.register(SelfEmployedOwnerAttachment)
admin.site.register(SelfEmployedOwnerNotes)
admin.site.register(CarEvent)
admin.site.register(InsuranceEvent)