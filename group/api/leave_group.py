import json
import threading

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from account.api import get_user, send_invitation
from account.models import Group, User


@csrf_exempt
@get_user.get_user
@require_http_methods(["POST"])
def leave_group(request, user):
    data = json.loads(request.body)
    group_id = int(data.get('group_id'))
    if not group_id:
        return JsonResponse({"message": "incomplete data"}, status=400)
    group = get_object_or_404(Group, id=group_id)
    if group.creator == user:
        group.delete()
    else:
        group.members.remove(user)

    return JsonResponse({"message": "ok"}, status=200)
