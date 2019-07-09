from os import name

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from account.api.get_user import get_user
from event.models import Place


@csrf_exempt
@get_user
@require_http_methods(["GET"])
def get_places(request, user):
    places = Place.objects.all()
    data =serialize_places(places)
    return JsonResponse(data, safe=False, status=200)


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
        data.append(serialized)
    return data
