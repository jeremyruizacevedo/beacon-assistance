from beacon.models import Beacon
from rest_framework import serializers


class BeaconSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beacon
        fields = '__all__'
