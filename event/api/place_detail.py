import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from account.api.get_user import get_user
from event.models import Event


@csrf_exempt
@require_http_methods(["GET"])
def place_detail(request):
    data = json.loads(request.body)
    place_id = data.get("place_id")
    try:
        place = Place.objects.get(id=int(place_id))
    except:
        return JsonResponse({"message": "Event not found"}, status=404)

    return JsonResponse(serialize_place(place))


def serialize_place(place):
    serialized = dict()
    serialized["id"] = place.pk
    serialized["name"] = place.name_en
    serialized["address"] = place.address.address_text
    serialized["city"] = place.city.name
    serialized["tags"] = [tag.name for tag in place.tags.all()]
    serialized["category"] = place.category.name_en
    images = place.images.all()
    serialized["images"] = [x.image.url for x in images] if images else ['/media/alt_image.jpeg']
    return serialized
