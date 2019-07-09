from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from account.api.get_user import get_user
from event.models import Event, Place


@csrf_exempt
@get_user
@require_http_methods(["GET"])
def retrieve_poll_data(request, user):
    e = Event.objects.all()
    p = Place.objects.all()
    data = []
    for i in e:
        data.append({"id": i.id, 'type': 'event'})
    for i in p:
        data.append({"id": i.id, 'type': 'place'})

    return JsonResponse(data, safe=False, status=200)
