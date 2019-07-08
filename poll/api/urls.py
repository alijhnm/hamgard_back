from poll.api.create_poll import create_text_poll, create_event_poll
from poll.api.retrieve_poll import get_group_polls, get_poll
from django.urls import path

urlpatterns = [
    path("createtextpoll/", create_text_poll),
    path('retrievepolls/', get_group_polls),
    path('createeventpoll/', create_event_poll),
    path('retrievepoll/', get_poll)
]
