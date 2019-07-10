from .models import Event, PersonEvent, EventType
from person.models import Person
from datetime import datetime


def create_person_event(person, event):
    person_event = None
    if not PersonEvent.objects.filter(person=person, event=event).exists():
        person_event = PersonEvent.objects.create(person=person, event=event)
    return person_event


def mark_assistance(person, event):
    person_event = PersonEvent.objects.filter(person=person, event=event)
    if person_event.exists() and person_event.last().status == 0:
        person_event_upd = person_event.last()
        person_event_upd.date = datetime.now()
        if event.start_time < datetime.now() and datetime.now() < event.end_time :
            person_event_upd.status = 1 # ASISTIO
        elif datetime.now() > event.end_time:
            person_event_upd.status = 2 # NO ASISTIO
        person_event_upd.save()
        return person_event_upd
    return None
