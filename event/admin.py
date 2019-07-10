from django.contrib import admin

from account.models import Vendor
from event.models import *

# Register your models here.
admin.site.register(Event)
admin.site.register(EventCategory)
admin.site.register(EventImage)
admin.site.register(EventVideo)
admin.site.register(Province)
admin.site.register(City)
admin.site.register(Address)
admin.site.register(PlaceCategory)
admin.site.register(Tag)
admin.site.register(Place)
admin.site.register(Vendor)
admin.site.register(PlaceImage)
