from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from account.api.get_user import get_user


@csrf_exempt
@get_user
@require_http_methods(['POST'])
def log_out(request, user):

    user.logout_user()
    return JsonResponse({"message": "Successfully logged out."}, status=200)

