from poll.api.create_poll import create_poll
from poll.api.retrieve_poll import get_group_polls, get_poll
from django.urls import path

urlpatterns = [
    path('retrievepolls/', get_group_polls),
    path('createeventpoll/', create_poll),
    path('retrievepoll/', get_poll)
]
