from django.urls import path, include

urlpatterns = [
    path('api/v1/', include('group.api.urls')),
    path('api/v1/poll/', include('poll.urls'))
]
