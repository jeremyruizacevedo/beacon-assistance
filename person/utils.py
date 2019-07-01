import requests
from oauth2_provider.models import AccessToken, Application
from django.contrib.auth.models import User
from .models import Person, Rol


def get_access_token(person, request):
    app = Application.objects.get(name="BEACON_APP")
    return requests.post('http://0.0.0.0:8000/o/token/',
                         data={
                             'grant_type': 'password',
                             'username': person.user.username,
                             'password': request.data['password'],
                             'client_id': app.client_id,
                             'client_secret': app.client_secret,
                         },
                         )


def create_username(obj):
    username = "{0}.{1}".format(obj["first_name"].split(" ")[0],
                                obj["last_name"].split(" ")[0])
    if User.objects.filter(username=username).exists():
        number = len(User.objects.filter(username__icontains=username+".")) + 1
        username = username + "." + str(number)
    return username


def create_person(obj):
    if obj["first_name"] and obj["last_name"] and obj["password"]:
        username = create_username(obj)
        user = User.objects.create_user(
            username=username, first_name=obj["first_name"], last_name=obj["last_name"], email=username+"@unmsm.edu.pe")
        user.set_password(obj["password"])
        user.save()
        person = Person.objects.create(
            user=user, rol=Rol.objects.get(name=obj["rol"]))
        return person
    return None
