from django.urls import path
from .login.customer import log_in as customer_login
from .logout.customer import log_out as customer_logout
from .signup.customer import sign_up as customer_signup


urlpatterns = [
    path('customerlogin/', customer_login),
    path('customerlogout/', customer_logout),
    path('customersignup/', customer_signup),
]
