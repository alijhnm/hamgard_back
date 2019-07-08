import json

from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from account.api.get_user import get_user
from account.models import Group
from event.models import Event, Place
from poll.models import *


@csrf_exempt
@get_user
@require_http_methods(["POST"])
def create_poll(request, user):
    data = json.loads(request.body)
    group_id = int(data.get("group_id"))
    place_ids = data.get("places")
    event_ids = list(map(int, data.get("events")))
    timeplan = data.get("timeplan")
    poll_question = data.get("question")
    group = get_object_or_404(Group, pk=group_id)

    if not group.creator.username == user.username:
        print("user", user.username)
        print("creator", group.creator.username)
        return JsonResponse({"message": "user not authorized to create poll"}, status=403)

    poll = Poll.objects.create(question=poll_question, timeplan=timeplan)

    for event_id in event_ids:
        event = Event.objects.filter(pk=int(event_id))
        if not event or len(event) > 1:
            continue
        PollChoice.objects.create(poll=poll, choice={'type': 'event', 'id': event_id})

    for place_id in place_ids:
        place = Place.objects.filter(pk=int(place_id))
        if not place or len(place) > 1:
            continue
        PollChoice.objects.create(poll=poll, choice={'type': 'place', 'id': place_id})

    group.polls.add(poll)
    group.save()

    return JsonResponse({"message": "Successfully created!"}, status=201)
