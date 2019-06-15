from django.urls import path
from .customer_login import log_in as customer_login
from .customer_logout import log_out as customer_logout
from .customer_signup import sign_up as customer_signup


urlpatterns = [
    path('customerlogin/', customer_login),
    path('customerlogout/', customer_logout),
    path('customersignup/', customer_signup),
]
