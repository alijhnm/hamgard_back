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
def retrieve_poll_data(request, user):
    group_id = request.GET.get('group_id', 1)
    a = random.randint(0, Event.objects.all().count()-6)
    e = Event.objects.all()[a:a+5]
    p = Place.objects.all()[a:a+5]
    data = []
    for i in e:
        data.append({"id": i.id, 'type': 'event'})
    for i in p:
        data.append({"id": i.id, 'type': 'place'})

    return JsonResponse(data, safe=False, status=201)
