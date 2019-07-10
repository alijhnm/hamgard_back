from django.urls import path

from poll.api.create_poll import create_poll
from poll.api.retrieve_poll import get_group_polls, get_poll, get_poll2
from poll.api.retrieve_poll_data import retrieve_poll_data
from poll.api.show_result import show_result
from poll.api.vote_in_poll import vote_in_poll


urlpatterns = [
    path('retrievepolls/', get_group_polls),
    path('createpoll/', create_poll),
    path('retrievepoll/', get_poll),
    path('retrievepolldata/', retrieve_poll_data),
    path('results/', show_result),
    path('vote/', vote_in_poll),
    path('retrievepoll2/', get_poll2)
]
