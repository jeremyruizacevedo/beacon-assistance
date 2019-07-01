from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Person, Rol
from .utils import create_username


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name',
                  'last_name', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }


class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = '__all__'


class PersonSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    rol = RolSerializer()

    class Meta:
        model = Person
        fields = '__all__'
