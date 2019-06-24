import requests
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from person.serializers import UserSerializer

CLIENT_ID = '2T7UFtSJkeeDhnnP3pjZe8et1M3F694tBuBG31F1'
CLIENT_SECRET = '1pfD5cuFzl2BY5DmomcOE2t4Y5fJHcwAzeer2dQqGoXY1DCXrMzA3eRMo5taClhTCfdDVBsvN666wzI47Y3oxvHLXE8RzpLphYxLABcZ9V6T5uhQBhJsWQA7zrbfEGxk'

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
            r = requests.post('http://0.0.0.0:8000/o/token/',
                              data={
                                  'grant_type': 'password',
                                  'username': request.data['username'],
                                  'password': request.data['password'],
                                  'client_id': CLIENT_ID,
                                  'client_secret': CLIENT_SECRET,
                              },
                              )
            return Response(r.json())
        else:
            # No backend authenticated the credentials
            return Response({"access_token": None})


class Register(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        '''
        Registers user to the server. Input should be in the format:
        {"first_name": "foo", "last_name": "bar" "password": "1234abcd"}
        '''
        # Put the data from the request into the serializer
        serializer = UserSerializer(data=request.data)
        # Validate the data
        if serializer.is_valid():
            # If it is valid, save the data (creates a user).
            serializer.save()
            return Response({})
            '''
            # Then we get a token for the created user.
            # This could be done differentley
            r = requests.post('http://0.0.0.0:8000/o/token/',
                              data={
                                  'grant_type': 'password',
                                  'username': request.data['username'],
                                  'password': request.data['password'],
                                  'client_id': CLIENT_ID,
                                  'client_secret': CLIENT_SECRET,
                              },
                              )
            return Response(r.json())
        return Response(serializer.errors)
        '''
        return Response({})
