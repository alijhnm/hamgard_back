import json

from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from account.models import Group
from poll.models import *
from account.api.get_user import get_user
from event.models import Event

@csrf_exempt
@get_user
@require_http_methods(["POST"])
def create_text_poll(request, user):
    data = json.loads(request.body)
    group_id = int(data.get("group_id"))
    poll_question = data.get("question")
    choices = data.get("choices")

    group = Group.objects.filter(pk=group_id).first()
    if not group:
        return JsonResponse({"message": "group not found"}, status=404)

    if not group.creator.username == user.username:
        print("user", user.username)
        print("creator", group.creator.username)
        return JsonResponse({"message": "user not authorized to create poll"}, status=401)

    poll = Poll.objects.create(question=poll_question)
    poll.save()

    for choice in choices:
        poll_choice = PollTextChoice.objects.create(text=choice, poll=poll)
        poll_choice.save()
        poll.choices.add(poll_choice)
        poll.save()

    group.polls.add(poll)
    group.save()

    print("question", poll.question)
    print("Choices:", poll.choices.all())

    return JsonResponse({"message": "Poll successfully created"}, status=200)


@csrf_exempt
@get_user
@require_http_methods(["POST", "GET"])
def create_event_poll(request, user):
    data = json.loads(request.body)
    group_id = int(data.get("group_id"))
    events_id = data.get("events")
    poll_question = data.get("question")

    group = Group.objects.filter(pk=group_id).first()
    if not group:
        return JsonResponse({"message": "group not found"}, status=404)

    if not group.creator.username == user.username:
        print("user", user.username)
        print("creator", group.creator.username)
        return JsonResponse({"message": "user not authorized to create poll"}, status=401)

    poll = Poll.objects.create(question=poll_question)

    for event_id in events_id:
        event = Event.objects.filter(pk=int(event_id)).first()
        if not event:
            continue
        event_choice = PollEventChoice.objects.create(event=event, poll=poll)
        event_choice.save()
        poll.event_choices.add(event_choice)
        poll.save()

    group.polls.add(poll)
    group.save()

    return JsonResponse({"message": "Successfully created poll"}, status=200)
