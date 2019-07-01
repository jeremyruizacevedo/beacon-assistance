from event.models import PersonEvent, Event, BeaconEvent, Place, EventType
from rest_framework import serializers


class EventTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventType
        fields = "__all__"


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = "__all__"


class EventSerializer(serializers.ModelSerializer):
    place = PlaceSerializer(read_only=True)
    event_type = EventTypeSerializer(read_only=True)
    class Meta:
        model = Event
        fields = '__all__'


class PersonEventSerializer(serializers.ModelSerializer):
    event = EventSerializer(read_only=True)
    class Meta:
        model = PersonEvent
        fields = '__all__'


class BeaconEventSerializer(serializers.ModelSerializer):
    event = EventSerializer(read_only=True)
    class Meta:
        model = BeaconEvent
        fields = '__all__'
