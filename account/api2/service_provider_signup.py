import json
from django.contrib.auth import authenticate
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from account.models import Vendor


@csrf_exempt
@require_http_methods(['POST'])
def sign_up(request):
    data = json.loads(request.body)
    username = data.get('username')
    password = data.get('password')
    national_number = data.get("national_number")
    business_licence = data.get("business_licence")
    name = data.get("name")

    user = authenticate(usernaem=username, password=password)

    if (national_number is None) \
            or (name is None) \
            or (business_licence is None):
        return JsonResponse({"message": "invalid params give"}, status=400)

    vendor = Vendor(
                user=user,
                national_number=national_number,
                business_licence=business_licence,
                name=name
                )
    vendor.save()
    return JsonResponse({"message": "Vendor is created successfully"})

