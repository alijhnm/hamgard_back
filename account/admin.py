from django.contrib import admin

from account.models import *

# Register your models here.

admin.site.register(User)
admin.site.register(Group)
admin.site.register(Profile)
# admin.site.register(Vendor)