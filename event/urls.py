from django.urls import path

from . import views

urlpatterns = [
    path('events/', views.EventViewSet.as_view({'get': 'list'})),
    path('person-event/', views.PersonEventViewSet.as_view({'get': 'list'})),
]