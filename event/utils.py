from .models import Event, PersonEvent, EventType
from person.models import Person
from datetime import datetime


def create_person_event(person, event):
    person_event = None
    if not PersonEvent.objects.filter(person=person, event=event).exists():
        person_event = PersonEvent.objects.create(person=person, event=event)
    return person_event


def mark_assistance(person, event):
    person_event = None
    if event.start_time > datetime.now() and event.end_time < datetime.now():
        person_event = PersonEvent.objects.filter(person=person, event=event)
        if person_event.exists() and person_event.last().status == 0:
            person_event.date = datetime.now()
            person_event.status = 1
            person_event.save()
    return person_event
