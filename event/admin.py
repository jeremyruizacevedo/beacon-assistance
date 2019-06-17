from django.contrib import admin

# Register your models here.

from event.models import Assistance, Event, BeaconEvent

admin.site.register(Assistance)
admin.site.register(Event)
admin.site.register(BeaconEvent)
