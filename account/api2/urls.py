from django.urls import path
from .service_provider_login import log_in as service_provider_login
from .service_provider_logout import log_out as service_provider_logout
from .service_provider_signup import sign_up as service_provider_signup


urlpatterns = [
    path('service_providerlogin/', service_provider_login),
    path('service_providerlogout/', service_provider_logout),
    path('service_providersignup/', service_provider_signup),

]
