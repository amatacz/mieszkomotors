from rest_framework import serializers

from mieszkomotors.models.car import Car, CarOwner
from mieszkomotors.models.events import CarEvent, InsuranceEvent, GenericEvent
from mieszkomotors.models.insurance import Insurance
from mieszkomotors.models.owner import Customer, IndividualCustomer, SelfEmployedCustomer, EnterpriseCustomer

class CarEventsSerializer(serializers.ModelSerializer):
    publication_datetime = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    update_datetime = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = CarEvent
        fields = "__all__"

class InsuranceEventsSerializer(serializers.ModelSerializer):
    publication_datetime = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    update_datetime = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = InsuranceEvent
        fields = "__all__"

class GenericEventSerializer(serializers.ModelSerializer):
    publication_datetime = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    update_datetime = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = GenericEvent
        fields = "__all__"
    
class CarSerializer(serializers.ModelSerializer):
    publication_datetime = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    update_datetime = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Car
        fields = "__all__"

class CarOwnerSerializer(serializers.ModelSerializer):
    publication_datetime = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    update_datetime = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = CarOwner
        fields = "__all__"

class InsuranceSerializer(serializers.ModelSerializer):
    publication_datetime = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    update_datetime = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Insurance
        fields = "__all__"

class CustomerSerializer(serializers.ModelSerializer):
    publication_datetime = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    update_datetime = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Customer
        fields = "__all__"

class IndividualCustomerSerializer(serializers.ModelSerializer):
    publication_datetime = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    update_datetime = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = IndividualCustomer
        fields = "__all__"

class SelfEmployedCustomerSerializer(serializers.ModelSerializer):
    publication_datetime = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    update_datetime = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = SelfEmployedCustomer
        fields = "__all__"

class EnterpriseCustomerSerializer(serializers.ModelSerializer):
    publication_datetime = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    update_datetime = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = EnterpriseCustomer
        fields = "__all__"

