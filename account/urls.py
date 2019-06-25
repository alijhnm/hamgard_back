from django.urls import path, include

urlpatterns = [
    path('api/', include('account.api2.urls'))
]
