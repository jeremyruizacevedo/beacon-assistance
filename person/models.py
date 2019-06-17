from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Rol(models.Model):
    """ Rol Model """
    name = models.CharField(max_length=30)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Person(models.Model):
    """ Person Model """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    codigo = models.CharField(max_length=8, default='')

    def __str__(self):
        return self.rol.name + ": " + self.user.username
