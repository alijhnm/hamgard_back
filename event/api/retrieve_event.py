import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .get_vendor import get_vendor
from event.models import Event


@csrf_exempt
@require_http_methods(["GET"])
def events_list(request, vendor):
    events = Event.objects.filter(vendor=vendor)
    return JsonResponse({"events": [serialize_event(event) for event in events]})


@csrf_exempt
@require_http_methods(["GET"])
def event_detail(request):
    data = json.loads(request.body)
    event_id = data.get("event_id")
    event = Event.objects.filter(id=event_id).first()
    if not event:
        return JsonResponse({"message": "Event not found"}, status=404)

    if event.vendor != vendor:
        return JsonResponse({"message": "Not vendor of this event."}, status=403)
    
    return JsonResponse(serialize_event(event))


def serialize_event(event):
    images = event.images.all()
    serialized = dict()
    serialized["id"] = event.id
    serialized["vendor"] = event.vendor.user.username
    serialized["title"] = event.title
    serialized["category"] = event.category.title
    serialized["summary"] = event.summary
    serialized["price"] = event.price
    serialized["discount"] = event.discount
    serialized["address"] = event.address.address_text
    serialized["images"] = [x.image.url for x in images] if images else ['/media/alt_image.jpeg']
    return serialized
