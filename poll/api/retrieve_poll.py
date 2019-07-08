import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from account.api.get_user import get_user
from account.models import Group


@csrf_exempt
@get_user
@require_http_methods(["GET"])
def get_group_polls(request, user):
    """Gets group_id in request's body and requester's token in request's head. Checks whether the user is authorized
    to see polls or not (the requester should be either group creator or group member). Then returns groups available
    polls to requester."""

    data = json.loads(request.body)

    group_id = data.get("group_id")
    group = Group.objects.filter(pk=group_id).first()

    # Invalid group_id given.
    if not group:
        return JsonResponse({"message": "group not found"}, status=404)

    if (user not in group.members.all()) and (user.username != group.creator.username):
        print("user", user.username)
        print("creator", group.creator.username)
        return JsonResponse({"message": "User not authorized to see this group's polls"}, status=401)

    polls = group.polls.all()
    return JsonResponse({"group_id": group.pk,
                         "group_name": group.name,
                         "polls": serialize_polls(polls)})


def serialize_polls(polls_queryset):
    """Serializes polls to be representable and shippable. Gets specific groups polls queryset and returns a list
    of polls with representable attributes."""

    result = list()
    for poll in polls_queryset:
        poll_dict = dict()
        poll_dict["id"] = poll.pk
        poll_dict["question"] = poll.question
        choices = [{"id": ch.id, "text": ch.text, "vote_count": ch.choice_count} for ch in poll.choices.all()]
        poll_dict["choices"] = choices
        result.append(poll_dict)

    return result
