from django.shortcuts import render
from rest_framework import viewsets
from event.serializers import EventSerializer, AssistanceSerializer
from event.models import Event, Assistance

# Create your views here.

class EventViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows event to be viewed or edited.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class AssistanceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows event to be viewed or edited.
    """
    queryset = Assistance.objects.all()
    serializer_class = AssistanceSerializer
