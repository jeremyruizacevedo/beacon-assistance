import requests
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .serializers import UserSerializer, PersonSerializer
from oauth2_provider.models import AccessToken, Application
from .models import Person, Rol
from .utils import get_access_token, create_person

# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class Login(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        '''
        Login user to the server. Input should be in the format:
        {"username": "username", "password": "1234abcd"}
        '''
        user = authenticate(
            username=request.data['username'], password=request.data['password'])
        if user is not None:
            # A backend authenticated the credentials
            # Then we get a token for the created user.
            # This could be done differentley
            app = Application.objects.get(name="BEACON_APP")
            access_token = AccessToken.objects.filter(
                user=user, application=app, expires__gte=datetime.now())
            if access_token.exists() and len(access_token) == 1:
                AccessToken.objects.filter(user=user, application=app, expires__lte=datetime.now()).delete()
                response = {
                    "person": PersonSerializer(user.person).data,
                    "access_token": access_token.last().token
                }
            else:
                AccessToken.objects.filter(user=user, application=app).delete()
                r = get_access_token(user.person, request)
                response = {
                    "person": PersonSerializer(user.person).data,
                    "access_token": r.json()["access_token"]
                }
            return Response(response)
        else:
            # No backend authenticated the credentials
            return Response({"person": None})


class Register(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        '''
        Registers user to the server. Input should be in the format:
        {"first_name": "foo", "last_name": "bar" "password": "1234abcd"}
        '''
        person = create_person(request.data)
        if person:
            r = get_access_token(person,request)
            response = {
                "person": PersonSerializer(person).data,
                "access_token": r.json()["access_token"]
            }
            return Response(response)
        return Response({"person": None})
