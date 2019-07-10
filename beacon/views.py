from django.shortcuts import render
from rest_framework import viewsets
from beacon.serializers import BeaconSerializer
from beacon.models import Beacon
from rest_framework import authentication, permissions

# Create your views here.

class BeaconViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows event to be viewed or edited.
    """
    permission_classes = [permissions.AllowAny]
    queryset = Beacon.objects.all()
    serializer_class = BeaconSerializer