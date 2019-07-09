import json
from django.http.response import JsonResponse
from django.db.utils import IntegrityError
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from account.models import Vendor


@csrf_exempt
@require_http_methods(['POST'])
def sign_up(request):
    data = json.loads(request.body)
    user = data.get('user')
    national_number = data.get('national_number')
    business_license = data.get("business_license")
    name = data.get("name")

    if (user is None)\
            or (national_number is None) \
            or (business_license is None) \
            or (name is None):
            return JsonResponse({"message": "invalid params give"}, status=400)

    user = Vendor(
                user=user,
                national_number=national_number,
                business_license=business_license,
                name=name,
                )
    try:
        user.save()
    except IntegrityError:
        return JsonResponse({'message': "Username already taken."}, status=400)

