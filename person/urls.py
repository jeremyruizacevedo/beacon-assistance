from django.urls import path

from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('users/', views.UserViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('login/', views.Login.as_view()),
    path('register/', views.Register.as_view()),
]