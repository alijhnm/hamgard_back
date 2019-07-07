from poll.api.create_poll import create_poll
from poll.api.retrieve_poll import get_group_polls
from django.urls import path

urlpatterns = [
    path("createpoll/", create_poll),
    path('retrievepoll/', get_group_polls)
]