from django.contrib import admin
from import_export import resources
from mieszkomotors.models.car import Car, CarOwner
from mieszkomotors.models.events import CarEvent, InsuranceEvent, \
    GenericEvent, WinterTyresReplacementEvent, \
    SpringTyresReplacementEvent, CarEventMail, \
    InsuranceEventMail, GenericEventMail
from mieszkomotors.models.insurance import Insurance, InsurancePartialPayments
from mieszkomotors.models.owner import Customer, CustomerAttachment, \
    CustomerNote, EnterpriseCustomer, SelfEmployedCustomer, IndividualCustomer


class IndividualCustomerResource(resources.ModelResource):
    class Meta:
        model = IndividualCustomer
        fields = ('id', 'first_name', 'last_name', 'email',
                  'phone_number', 'address_prefix', 'street', 'building',
                  'apartment', 'city', 'zip_code', 'pesel',
                  'driving_license_since', 'customer_type', 'client_since')
        export_order = ('id', 'first_name', 'last_name', 'email',
                        'phone_number', 'address_prefix', 'street', 'building',
                        'apartment', 'city', 'zip_code', 'pesel',
                        'driving_license_since', 'customer_type',
                        'client_since')


class SelfEmployedCustomerResource(resources.ModelResource):
    class Meta:
        model = SelfEmployedCustomer
        fields = ('id', 'first_name', 'last_name', 'email',
                  'phone_number', 'address_prefix', 'street', 'building',
                  'apartment', 'city', 'zip_code', 'pesel', 'nip', 'regon',
                  'driving_license_since', 'customer_type', 'client_since')
        export_order = ('id', 'first_name', 'last_name', 'email',
                        'phone_number', 'address_prefix', 'street', 'building',
                        'apartment', 'city', 'zip_code', 'pesel', 'nip',
                        'regon', 'customer_type',
                        'client_since')


class EnterpriseCustomerResource(resources.ModelResource):
    class Meta:
        model = EnterpriseCustomer
        fields = ('id', 'company_name', 'nip', 'email',
                  'phone_number', 'address_prefix', 'street', 'building',
                  'apartment', 'city', 'zip_code',
                  'driving_license_since', 'customer_type', 'client_since')
        export_order = ('id', 'company_name', 'nip', 'email',
                        'phone_number', 'address_prefix', 'street', 'building',
                        'apartment', 'city', 'zip_code', 'customer_type',
                        'client_since')


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
admin.site.register(WinterTyresReplacementEvent)
admin.site.register(SpringTyresReplacementEvent)

admin.site.register(CarEventMail)
admin.site.register(GenericEventMail)
admin.site.register(InsuranceEventMail)
