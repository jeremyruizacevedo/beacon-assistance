from event.models import Assistance, Event
from rest_framework import serializers


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class AssistanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assistance
        fields = '__all__'