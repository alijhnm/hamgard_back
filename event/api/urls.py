from .retrieve_event import *
from .create_event import create_event
from .get_place import get_places
from django.urls import path

urlpatterns = [
    path('createevent/', create_event),
    path('events/', events_list),
    path('event/', event_detail),
    path('places/', get_places)
]
