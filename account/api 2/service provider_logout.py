import json
from django.contrib.auth import authenticate
from django.http import JsonResponse
from .utils import get_user
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods


@get_user
@csrf_exempt
@require_http_methods(['POST'])
def log_out(request, user):
    if user:
        user.logout_user()
        return JsonResponse({"message": "Logged out successfully "}, status=200)
    else:
        return JsonResponse({"message": "User not found !"}, status=404)
