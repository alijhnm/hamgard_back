import json
from django.contrib.auth import authenticate
from django.http import JsonResponse


def log_in(request):
    data = json.loads(request.body)
    username = data.get('username')
    password = data.get('password')

    if username is None or password is None:
        return JsonResponse({"message": "Invalid username or password !"}, status=400)

    user = authenticate(username=username, password=password)
    if not user:
        return JsonResponse({"message": "Incorrect username or password !"}, status=404)