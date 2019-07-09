from django.urls import path, include
from .create_group import create_group
from .retrieve_group import group_detail, group_list
from .group_users import group_users

urlpatterns = [
    path('create_group/', create_group),
    path('groups/', group_list),
    path('group/', group_detail),
    path('members/<int:group_id>/', group_users,
         name='group_members'),
]
