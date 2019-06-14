from django.urls import path, include
from .create_group import create_group
from.retrieve_group import group_detail, group_list

urlpatterns = [
    path('creategroup/', create_group),
    path('groups/', group_list),
    path('group/', group_detail)
]
