import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from account.models import *
from account.api.get_user import get_user


@csrf_exempt
@get_user
@require_http_methods(["GET"])
def group_list(request, user):
    groups1 = Group.objects.filter(members__in=[user])
    groups2 = Group.objects.filter(creator=user)
    groups = list(groups1) + list(groups2)
    return JsonResponse({"user_groups": serialize_group_queryset(groups)})


@get_user
@csrf_exempt
@require_http_methods(["GET"])
def group_detail(request, user):
    data = json.loads(request.body)
    group_id = data.get("group_id")
    group = Group.objects.filter(id=group_id).first()
    if user not in group.members.all() and group.creator.username != user.username:
        return JsonResponse({"message": "user not in requested group."}, status=401)

    if group is None:
        return JsonResponse({"message": "Group not found."}, status=400)

    return JsonResponse({"name": group.name,
                         "created": group.created,
                         "type": group.type,
                         "creator": group.creator.username,
                         "members": [member.username for member in group.members.all()]}, status=200)


def serialize_group_queryset(queryset):
    result = list()
    for group in queryset:
        serialized = dict()
        serialized["name"] = group.name
        serialized["creator"] = group.creator.username
        serialized["created"] = group.created
        serialized["type"] = group.type
        serialized["members"] = [user.username for user in group.members.all()]

        result.append(serialized)
    return result
