from rest_framework import serializers
from mieszkomotors.models.events import CarEvent, InsuranceEvent
from mieszkomotors.models.car import Car, CarOwner
from mieszkomotors.models.insurance import Insurance
from mieszkomotors.models.owner import Customer, IndividualCustomer, SelfEmployedCustomer, EnterpriseCustomer

class CarEventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarEvent
        fields = "__all__"

class InsuranceEventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = InsuranceEvent
        fields = "__all__"
    
class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        exclude = ('publication_datetime', 'update_datetime', 'created_by')

class CarOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarOwner
        exclude = ('publication_datetime', 'update_datetime', 'created_by')

class InsuranceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insurance
        exclude = ('publication_datetime', 'update_datetime', 'created_by')

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        exclude = ('publication_datetime', 'update_datetime', 'created_by')

class IndividualCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndividualCustomer
        exclude = ('publication_datetime', 'update_datetime', 'created_by')

class SelfEmployedCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = SelfEmployedCustomer
        exclude = ('publication_datetime', 'update_datetime', 'created_by')

class EnterpriseCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnterpriseCustomer
        # exclude = ('publication_datetime', 'update_datetime', 'created_by')
        fields = "__all__"

