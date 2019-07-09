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
def vote_in_poll(request, user):
    data = json.loads(request.body)
    poll_id = int(data.get("poll_id"))
    group_id = int(data.get("group_id"))
    choice_ids = list(map(int, data.get("choices")))
    group = get_object_or_404(Group, pk=group_id)
    try:
        if user not in group.members.all():
            raise Exception
        poll = group.polls.get(id=int(poll_id))
    except ObjectDoesNotExist:
        return JsonResponse({"message": "poll does not exist"}, status=404)
    except Exception:
        return JsonResponse({"message": "bad request"}, status=400)

    choices = PollChoice.objects.filter(id__in=choice_ids)

    for c in choices:
        if not c.is_voted_user(user):
            x.members.add(user)
        else:
            x.members.remove(user)

    return JsonResponse({"message": "Successfully voted!"}, status=200)
