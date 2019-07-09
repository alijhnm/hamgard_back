import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from account.api.get_user import get_user
from account.models import Group
from event.models import Event, Place
from poll.models import Poll


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


@csrf_exempt
@get_user
@require_http_methods(["POST", "GET"])
def get_poll(request, user):
    data = json.loads(request.body)
    poll_id = data.get("id")
    group_id = data.get("group_id")

    group = Group.objects.filter(pk=group_id).first()
    if not group:
        return JsonResponse({"message": "Group not found"}, status=404)

    poll = Poll.objects.filter(pk=poll_id).first()
    if not poll:
        return JsonResponse({"message": "Poll not found"}, status=404)

    if (user not in group.members.all()) and (user.username != group.creator.username):
        print("user", user.username)
        print("creator", group.creator.username)
        return JsonResponse({"message": "User not authorized to see this group's polls"}, status=401)

    choices = list()
    for choice in poll.choices.all():
        data = dict()
        if choice.choice.get("type") == "event":
            try:
                event = Event.objects.get(pk=choice.choice.get("id"))
            except:
                continue

            data["type"] = "event"
            data["id"] = event.pk
            data["title"] = event.title
            data["tags"] = [tag.name for tag in event.tags.all()]
            data["discount"] = event.discount
            data["price"] = event.price
            data["summary"] = event.summary
            data["vote_count"] = len(choice.members.all())
            choices.append(data)

        elif choice.choice.get("type") == "place":
            try:
                place = Place.objects.get(pk=choice.choice.get("id"))
            except:
                continue

            data["id"] = place.pk
            data["type"] = "place"
            data["name"] = place.name_en
            data["city"] = place.city.name
            data["province"] = place.city.province.name
            data["vote_count"] = len(choice.members.all())
            choices.append(data)

    return JsonResponse({"id": poll.pk,
                         "question": poll.question,
                         "vote_count": poll.vote_count,
                         "choices": choices})


def serialize_polls(polls_queryset):
    """Serializes polls to be representable and shippable. Gets specific groups polls queryset and returns a list
    of polls with representable attributes."""

    result = list()
    for poll in polls_queryset:
        poll_dict = dict()
        poll_dict["id"] = poll.pk
        poll_dict["question"] = poll.question
        poll_dict["vote_count"] = poll.vote_count
        result.append(poll_dict)

    return result
