import json
from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods


@csrf_exempt
@require_http_methods(['POST'])
def log_in(request):
    data = json.loads(request.body)
    username = data.get('username')
    password = data.get('password')
    remember_me = data.get("remember_me")

    if username is None or password is None:
        return JsonResponse({"message": "Invalid username or password !"}, status=400)

    vendor = authenticate(username=username, password=password)

    if not vendor:
        return JsonResponse({"message": "Incorrect username or password !"}, status=404)

    if not remember_me:
        param = False
    else:
        param = True

        if vendor.token is not None:
            return JsonResponse({"token": "token " + vendor.token})

        token = vendor.login(remember_me=param)
        return JsonResponse({"token": "token " + token}, status=200)