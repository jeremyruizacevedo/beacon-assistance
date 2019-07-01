from django.contrib import admin

# Register your models here.

from event.models import PersonEvent, Event, BeaconEvent, EventType, EventImage, Place

admin.site.register(BeaconEvent)
admin.site.register(Event)
admin.site.register(EventImage)
admin.site.register(EventType)
admin.site.register(PersonEvent)
admin.site.register(Place)
