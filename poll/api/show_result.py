import json
from random import random

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
@require_http_methods(["GET"])
def show_result(request, user):
    poll_id = request.GET.get('poll_id')
    try:
        poll = Poll.objects.get(id=int(id))
    except:
        return JsonResponse({"message": "not found"}, status=404)
    choices = poll.choices.all()
    resolved_choices = []
    for c in choices:
        t = c.data["type"]
        i = c.data["id"]
        try:
            if t == "event":
                e = Event.objects.get(id=int(i))
            else:
                e = Place.objects.get(id=int(i))
        except:
            return JsonResponse({"message": "some thing went wrong"}, status=500)
        data = {"type": t, "id": i, "title": e.title}
        resolved_choices.append(data)
    data = {"choices": resolved_choices, "vote_counts": poll.vote_counts, 
            "id": poll.id, "question": poll.question, "time_plan": poll.time_plan}
            
    return JsonResponse(data, safe=False, status=200)
