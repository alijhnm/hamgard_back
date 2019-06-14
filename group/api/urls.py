from django.urls import path, include
from .create_group import create_group

urlpatterns = [
    path('creategroup/', create_group),
]
