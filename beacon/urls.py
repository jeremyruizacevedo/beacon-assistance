from django.urls import path

from . import views

urlpatterns = [
    path('beacons/', views.BeaconViewSet.as_view({'get': 'list'})),
]