from django.shortcuts import render
from rest_framework import viewsets
from event.serializers import EventSerializer, PersonEventSerializer
from event.models import Event, PersonEvent

# Create your views here.

class EventViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows event to be viewed or edited.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class PersonEventViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows event to be viewed or edited.
    """
    queryset = PersonEvent.objects.all()
    serializer_class = PersonEventSerializer
