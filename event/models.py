from django.db import models
from person.models import Person
from beacon.models import Beacon
from django.utils import timezone

# Create your models here.


class EventType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Place(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        if self.description is None or self.description == "":
            description = ""
        else:
            description = " (" + self.description + ")"
        return self.name + description


class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    topic = models.CharField(max_length=50, blank=True, null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    event_type = models.ForeignKey(
        EventType, on_delete=models.CASCADE, blank=True, null=True)
    place = models.ForeignKey(
        Place, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name


class PersonEvent(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.person.user.get_full_name() + ' - ' + self.event.name + " : " + str(self.date)


class BeaconEvent(models.Model):
    beacon = models.ForeignKey(Beacon, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return self.event.name + ' --> ' + self.beacon.uuid


class EventImage(models.Model):
    event = models.ForeignKey(
        Event, on_delete=models.CASCADE, blank=True, null=True)
    image_url = models.CharField(max_length=200)

    def __str__(self):
        return self.event.name + " --> " + self.image_url
