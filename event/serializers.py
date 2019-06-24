from event.models import PersonEvent, Event
from rest_framework import serializers


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class PersonEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonEvent
        fields = '__all__'