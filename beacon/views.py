from django.shortcuts import render
from rest_framework import viewsets
from beacon.serializers import BeaconSerializer
from beacon.models import Beacon

# Create your views here.

class BeaconViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows event to be viewed or edited.
    """
    queryset = Beacon.objects.all()
    serializer_class = BeaconSerializer