from django.urls import path

from .search_event import search_event

from .create_event import create_event
from .get_place import get_places
from .retrieve_event import *
from .search_place import search_place

urlpatterns = [
    path('createevent/', create_event),
    path('events/', events_list),
    path('event/', event_detail),
    path('places/', get_places),
    path('places/search/', search_place),
    path('events/search/', search_event)

]
