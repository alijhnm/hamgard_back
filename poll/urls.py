from django.urls import path, include

urlpatterns = [
    path('', include("poll.api.urls"))
]