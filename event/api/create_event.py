import json
from account.api import get_user
from account.models import Vendor
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from event.models import *
from .get_vendor import get_vendor


@csrf_exempt
@get_vendor
@require_http_methods(["POST"])
def create_event(request, vendor):
    """
    Creates an event with respect to given parameters in request. Retrieves vendor by using @get_user
    decorator from account app. If a provided tag in not yet available in database, will be created and
    available from now on for new events to be created. Does the same for provided category. Creates a new
    Address object for any new event.
    Returns a serialized view of the created event.
    """
    data = json.loads(request.body)

    title = data.get("title")
    category_tittle = data.get("category")
    summary = data.get("summary")
    discount = data.get("discount")
    price = data.get("price")
    tag_titles = data.get("tags")
    address_text = data.get("address")

    event_tags = list()
    for tag_title in tag_titles:
        tag = Tag.objects.filter(name=tag_title).first()
        if tag:
            event_tags.append(tag)
        else:
            tag = Tag.objects.create(name=tag_title)
            tag.save()
            event_tags.append(tag)

    category = EventCategory.objects.filter(title=category_tittle).first()
    if not category:
        category = EventCategory.objects.create(title=category_tittle)
        category.save()

    address = Address.objects.create(address_text=address_text)
    address.save()

    event = Event.objects.create(vendor=vendor,
                                 title=title,
                                 category=category,
                                 summary=summary,
                                 discount=discount,
                                 price=price,
                                 address=address)
    event.save()

    for tag in event_tags:
        event.tags.add(tag)
        event.save()

    return JsonResponse({"status": "Successfully created event.",
                         "creator_id": vendor.user.pk,
                         "event id": event.pk,
                         "name": event.title,
                         "price": event.price,
                         "category": event.category.title,
                         "discount": event.discount,
                         "tags": [tag_title.name for tag_title in event_tags],
                         })
