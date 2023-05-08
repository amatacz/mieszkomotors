from django.contrib import admin

from mieszkomotors.models.car import Car, CarOwner
from mieszkomotors.models.events import CarEvent, InsuranceEvent, GenericEvent, GenericEventMail, CarEventMail, InsuranceEventMail
from mieszkomotors.models.insurance import Insurance, InsurancePartialPayments
from mieszkomotors.models.owner import Customer, CustomerAttachment, CustomerNote, EnterpriseCustomer, SelfEmployedCustomer, IndividualCustomer



admin.site.register(Car)
admin.site.register(CarEvent)
admin.site.register(CarOwner)

admin.site.register(Insurance)
admin.site.register(InsuranceEvent)
admin.site.register(InsurancePartialPayments)

admin.site.register(Customer)
admin.site.register(CustomerAttachment)
admin.site.register(CustomerNote)
admin.site.register(IndividualCustomer)
admin.site.register(SelfEmployedCustomer)
admin.site.register(EnterpriseCustomer)

admin.site.register(GenericEvent)

admin.site.register(CarEventMail)
admin.site.register(GenericEventMail)
admin.site.register(InsuranceEventMail)