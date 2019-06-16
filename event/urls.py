from .api.create_event import create_event
from django.urls import path


urlpatterns = [
    path('createevent/', create_event)
]
