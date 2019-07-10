import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from account.models import *
from account.api.get_user import get_user
from django.db.models import Q
from poll.api.retrieve_poll import serialize_polls


def serialize_group_queryset(queryset, user=None):
    result = list()
    for group in queryset:
        serialized = dict()
        serialized["name"] = group.name
        serialized["id"] = group.pk
        serialized["admin_email"] = group.creator.email
        serialized["admin_id"] = group.creator.id
        serialized["admin_username"] = group.creator.username
        serialized["created"] = group.created
        serialized["type"] = group.type
        serialized["members"] = [{"username": user.username,
                                  "id": user.id, "email": user.email,
                                  "first_name": user.first_name,
                                  "last_name": user.last_name} for user in group.members.all()]
        serialized["members_count"] = group.members.all().count() + 1
        serialized["summary"] = group.summary
        serialized['is_admin'] = True if user == group.creator else False
        result.append(serialized)
    return result


@csrf_exempt
@get_user
@require_http_methods(["GET"])
def group_list(request, user):
    groups = Group.objects.filter(Q(creator=user) | Q(members__in=[user]))
    result = serialize_group_queryset(groups, user=user)
    return JsonResponse(result, safe=False, status=200)


@csrf_exempt
@get_user
@require_http_methods(["GET", "POST"])
def group_detail(request, user):
    data = json.loads(request.body)
    group_id = data.get("group_id")
    group = Group.objects.filter(id=group_id).first()

    if group is None:
        return JsonResponse({"message": "Group not found."}, status=400)

    if user not in group.members.all() and group.creator.username != user.username:
        return JsonResponse({"message": "user not in requested group."}, status=401)

    polls = group.polls.all()
    print(group.creator.username == user.username)
    return JsonResponse({"name": group.name,
                         "id": group.pk,
                         "created": group.created,
                         "type": group.type,
                         "is_creator": group.creator.username == user.username,
                         "creator": group.creator.username,
                         "polls": serialize_polls(polls),
                         "members": [{"key": str(i), "username": member.username} for i, member in enumerate(group.members.all())]}, status=200)
