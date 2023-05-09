from rest_framework import viewsets, permissions

from mieszkomotors.models.events import CarEvent, InsuranceEvent
from mieszkomotors.models.car import Car, CarOwner
from mieszkomotors.models.events import GenericEvent
from mieszkomotors.serializers import *
from mieszkomotors.permissions import IsStaffOrReadOnly

class CarEventsViewset(viewsets.ModelViewSet):
    queryset = CarEvent.objects.all()
    serializer_class = CarEventsSerializer
    permission_classes = [permissions.IsAuthenticated, IsStaffOrReadOnly]

class InsuranceEventsViewset(viewsets.ModelViewSet):
    queryset = InsuranceEvent.objects.all()
    serializer_class = InsuranceEventsSerializer
    permission_classes = [permissions.IsAuthenticated, IsStaffOrReadOnly]

class CarViewset(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [permissions.IsAuthenticated, IsStaffOrReadOnly]

class CarOwnerViewset(viewsets.ModelViewSet):
    queryset = CarOwner.objects.all()
    serializer_class = CarOwnerSerializer
    permission_classes = [permissions.IsAuthenticated, IsStaffOrReadOnly]
    
class InsuranceViewset(viewsets.ModelViewSet):
    queryset = Insurance.objects.all()
    serializer_class = InsuranceSerializer
    permission_classes = [permissions.IsAuthenticated, IsStaffOrReadOnly]

class CustomerViewset(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [permissions.IsAuthenticated, IsStaffOrReadOnly]

class IndividualCustomerViewset(viewsets.ModelViewSet):
    queryset = IndividualCustomer.objects.all()
    serializer_class = IndividualCustomerSerializer
    permission_classes = [permissions.IsAuthenticated, IsStaffOrReadOnly]

class SelfEmployedCustomerViewset(viewsets.ModelViewSet):
    queryset = SelfEmployedCustomer.objects.all()
    serializer_class = SelfEmployedCustomerSerializer
    permission_classes = [permissions.IsAuthenticated, IsStaffOrReadOnly]

class EnterpriseCustomerViewset(viewsets.ModelViewSet):
    queryset = EnterpriseCustomer.objects.all()
    serializer_class = EnterpriseCustomerSerializer
    permission_classes = [permissions.IsAuthenticated, IsStaffOrReadOnly]

class GenericEventsViewset(viewsets.ModelViewSet):
    queryset = GenericEvent.objects.all()
    serializer_class = GenericEventSerializer
    permission_classes = [permissions.IsAuthenticated, IsStaffOrReadOnly]

