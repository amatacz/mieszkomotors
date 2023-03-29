from rest_framework import viewsets
from rest_framework import generics

from mieszkomotors.models.events import CarEvent, InsuranceEvent
from mieszkomotors.models.car import Car
from mieszkomotors.serializers import CarEventsSerializer, InsuranceEventsSerializer, CarSerializer

class CarEventsViewset(viewsets.ModelViewSet):
    queryset = CarEvent.objects.all()
    serializer_class = CarEventsSerializer

class InsuranceEventsViewset(viewsets.ModelViewSet):
    queryset = InsuranceEvent.objects.all()
    serializer_class = InsuranceEventsSerializer

class CarViewset(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    