from django.contrib import admin

# Register your models here.

from event.models import PersonEvent, Event, BeaconEvent, EventType

admin.site.register(BeaconEvent)
admin.site.register(Event)
admin.site.register(EventType)
admin.site.register(PersonEvent)
