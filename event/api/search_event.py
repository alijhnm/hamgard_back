import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .get_vendor import get_vendor
from event.models import Event
from event.models import Place
from account.api.get_user import get_user
from django.db.models import Q
# @csrf_exempt
# @get_vendor
# @require_http_methods(["GET"])
# def events_list(request, vendor):
#     events = Event.objects.filter(vendor=vendor)
#     return JsonResponse({"events": [serialize_event(event) for event in events]})


@csrf_exempt
@require_http_methods(["GET"])
def search_event(request):
    q = request.GET.get("q")
    event = Event.objects.filter(Q(title__icontains= q))
    if not event:
        return JsonResponse([], safe=False, status=200)
    return JsonResponse(serialize_event(event), safe=False, status=200)

def serialize_event(queryset):
    data = list()
    for event in queryset:
        serialized = dict()
        serialized["id"] = event.id
        serialized["vendor"] = event.vendor.user.username
        serialized["title"] = event.title
        serialized["category"] = event.category.title
        serialized["summary"] = event.summary
        serialized["price"] = event.price
        serialized["discount"] = event.discount
        serialized["address"] = event.address.address_text
        data.append(serialized)
    return data
