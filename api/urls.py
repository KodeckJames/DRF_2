from home.views import index, person
from django.urls import path

urlpatterns = [
    path('index/', index),
    path('person/', person)
]
