import json
from django.contrib.auth.hashers import make_password
from django.http.response import JsonResponse
from django.db.utils import IntegrityError
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from account.models import Vendor


@csrf_exempt
@require_http_methods(['POST'])
def sign_up(request):
    data = json.loads(request.body)
    username = data.get('username')
    password = data.get('password')
    company_name = data.get("company_name")
    first_name = data.get("first_name")
    last_name = data.get("last_name")
    service_provider_phone_number = data.get('service_provider_phone_number')
    company_phone_number = data.get("company_phone_number")
    email = data.get("email")

    if (username is None)\
            or (password is None) \
            or (company_name is None) \
            or (first_name is None) \
            or (last_name is None)\
            or (service_provider_phone_number is None)\
            or (company_phone_number is None)\
            or (email is None):
            return JsonResponse({"message": "invalid params give"}, status=400)

    user = Vendor(

                username=username,
                password=make_password(password),
                company_name=company_name,
                first_name=first_name,
                last_name=last_name,
                service_provider_phone_number=service_provider_phone_number,
                company_phone_number=company_phone_number,
                email=email
                )
    try:
        user.save()
    except IntegrityError:
        return JsonResponse({'message': "Username already taken."}, status=400)

