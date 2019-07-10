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


# @get_user
@csrf_exempt
@require_http_methods(["GET"])
def search_place(request):
    q = request.GET.get("q")
    places = Place.objects.filter(Q(name_fa__icontains= q) | Q(name_en__icontains= q))
    if not places:
        return JsonResponse([], safe=False, status=200)
    return JsonResponse(serialize_places(places), safe=False, status=200)

def serialize_places(queryset):
    data = list()
    for place in queryset:
        serialized = dict()
        serialized["id"] = place.pk
        serialized["name"] = place.name_en
        serialized["address"] = place.address.address_text
        serialized["city"] = place.city.name
        serialized["tags"] = [tag.name for tag in place.tags.all()]
        serialized["category"] = place.category.name_en
        images = place.images.all()
        serialized["images"] = [x.image.url for x in images] if images else ['/media/alt_image.jpeg']
        data.append(serialized)
    return data
