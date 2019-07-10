from django.shortcuts import render
from rest_framework import viewsets
from event.serializers import EventSerializer, PersonEventSerializer, BeaconEventSerializer
from event.models import Event, PersonEvent, BeaconEvent, EventType
from person.models import Person
from datetime import datetime
from .utils import create_person_event, mark_assistance
from rest_framework.throttling import UserRateThrottle

# Create your views here.


class EventViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows event to be viewed or edited.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class PersonEventViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows events of person to be viewed or edited.
    """
    queryset = PersonEvent.objects.all()
    serializer_class = PersonEventSerializer
    throttle_classes = (UserRateThrottle,)

    def get_queryset(self):
        queryset = []
        if "id_person" in self.request.query_params:
            person = Person.objects.get(
                id=self.request.query_params["id_person"])
            if "uuid_beacon" in self.request.query_params:
                print("uuid")
                list_id_events = BeaconEvent.objects.filter(
                    beacon__uuid=self.request.query_params["uuid_beacon"]).values_list('event', flat=True)
                list_events = Event.objects.filter(id__in=list_id_events)
                for event in list_events:
                    if event.event_type.name == "General":
                        create_person_event(person, event)
                    else:
                        mark_assistance(person, event)
                queryset = PersonEvent.objects.filter(person=person,
                                                      event__end_time__gte=datetime.now()).\
                                                order_by('event__start_time')
            elif "id_event" in self.request.query_params:
                queryset = PersonEvent.objects.filter(person=person,
                                                      event__id=self.request.query_params["id_event"],
                                                      event__end_time__gte=datetime.now()).\
                                                order_by('event__start_time')
            else:
                queryset = PersonEvent.objects.filter(person=person,
                                                      event__end_time__gte=datetime.now()).\
                                                order_by('event__start_time')
        else:
            queryset = PersonEvent.objects.all()
        return queryset


class BeaconEventViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows events of beacon to be viewed or edited.
    """
    queryset = BeaconEvent.objects.all()
    serializer_class = PersonEventSerializer

    def get_queryset(self):
        queryset = []
        if "uuid_beacon" in self.request.query_params and "id_person" in self.request.query_params:
            person = Person.objects.get(
                id=self.request.query_params["id_person"])
            list_id_events = BeaconEvent.objects.filter(
                beacon__uuid=self.request.query_params["uuid_beacon"]).values_list('event', flat=True)
            list_events = Event.objects.filter(id__in=list_id_events)
            for event in list_events:
                create_person_event(person, event)
        else:
            queryset = BeaconEvent.objects.all()
        return queryset
