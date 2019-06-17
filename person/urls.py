from django.urls import path

from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('users/', views.UserViewSet.as_view({'get': 'list'})),
]