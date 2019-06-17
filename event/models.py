from django.db import models
from person.models import Person

# Create your models here.


class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return self.name


class Assistance(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    state = models.IntegerField(default=True)

    def __str__(self):
        return self.person.user.username + ' --> ' + str(self.date)


class BeaconEvent(models.Model):
    beacon = models.ForeignKey(Person, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return self.event.name + ' --> ' + self.beacon.uuid
