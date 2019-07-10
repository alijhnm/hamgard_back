from django.contrib import admin

from poll.models import PollChoice, Poll

# Register your models here.
admin.site.register(Poll)
admin.site.register(PollChoice)