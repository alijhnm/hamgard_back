import json
from django.http.response import JsonResponse
from django.db.utils import IntegrityError
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from account.models import User


@csrf_exempt
@require_http_methods(['POST'])
def sign_up(request):
    """
    Retrieves essential fields for user creation. returns 'invalid params given' for missing fields.
    also returns 'Username already taken' if username is not unique.
    logs the user in, right after user creation.
    """
    data = json.loads(request.body)
    username = data.get('username')
    password = data.get('password')
    phone_number = data.get('phone_number')
    first_name = data.get("first_name")
    last_name = data.get("last_name")
    email = data.get("email")

    if (username is None)\
            or (password is None)\
            or (phone_number is None)\
            or (email is None)\
            or (first_name is None)\
            or (last_name is None):
        return JsonResponse({"message": "invalid params give"}, status=400)

    user = User(
                email=email,
                username=username,
                password=password,
                mobile_number=phone_number,
                first_name=first_name,
                last_name=last_name
                )
    try:
        user.save()
    except IntegrityError:
        return JsonResponse({'message': "Username already taken."}, status=400)
    token = user.login_user(remember_me=False)
    return JsonResponse({'token': "token " + token}, status=200)
