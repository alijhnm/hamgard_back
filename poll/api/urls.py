from poll.api.create_poll import create_poll
from django.urls import path

urlpatterns = [
    path("createpoll/", create_poll)
]