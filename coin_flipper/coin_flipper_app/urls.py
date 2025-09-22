from django.urls import path
from . import views

urlpatterns = [
    path('', views.flip_coin, name='flip_coin'),
]