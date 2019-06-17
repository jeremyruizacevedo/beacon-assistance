from django.contrib.auth.models import User, Group
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class PersonSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = User
        fields = '__all__'
