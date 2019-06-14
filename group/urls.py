from django.urls import path, include

urlpatterns = [
    path('', include('group.api.urls'))
]
