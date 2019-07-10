from event.models import PersonEvent, Event, BeaconEvent, Place, EventType, EventImage
from rest_framework import serializers


class EventTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventType
        fields = "__all__"


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = "__all__"


class EventImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventImage
        fields = "__all__"


class EventSerializer(serializers.ModelSerializer):
    event_type = EventTypeSerializer(read_only=True)
    place = PlaceSerializer(read_only=True)
    images = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Event
        exclude = ()

    def get_images(self, obj):
        return EventImageSerializer(EventImage.objects.filter(event=obj), many=True).data


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
