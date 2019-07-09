import json
from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods


@csrf_exempt
@require_http_methods(['POST'])
def log_out(request, vendor):
    if vendor:
        vendor.logout()
        return JsonResponse({"message": "Logged out successfully "}, status=200)
    else:
        return JsonResponse({"message": "User not found !"}, status=404)
