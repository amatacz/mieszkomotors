from rest_framework import serializers
from mieszkomotors.models.events import CarEvent, InsuranceEvent
from mieszkomotors.models.car import Car

class CarEventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarEvent
        # fields = ('id', 'car', 'title', 'start', 'end')
        fields = "__all__"


class InsuranceEventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = InsuranceEvent
        # fields = ('id', 'insurance', 'title', 'start', 'end')
        fields = "__all__"
    
class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"