import json

from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from account.api.get_user import get_user
from account.models import *


@csrf_exempt
@require_http_methods(['GET'])
def group_users(request, group_id):
    group = get_object_or_404(Group, id=group_id)
    group_members = group.members.all()
    data = dict(id=group.id, name=group.name, admin={'id': group.creator.id,
                                                     'name': group.creator.username,
                                                     'email': group.creator.email},
                members=[{"name": x.username, "id":x.id,
                          "email": x.email} for x in group_members])
    return JsonResponse(data, safe=False, status=200)
