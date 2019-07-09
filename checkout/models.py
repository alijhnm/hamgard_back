import os
import binascii

from django.db import models
from django.contrib.postgres.fields import JSONField

# Create your models here.


class Cart(models.Model):
    user = models.ForeignKey(
        'account.User', blank=True, null=True, related_name='carts',
        on_delete=models.CASCADE)
    token = models.CharField(max_length=100, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    last_change = models.DateTimeField(auto_now_add=True)
    is_ordered = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return str(self.token)

    class Meta:
        ordering = ('-last_change',)

    def __repr__(self):
        return 'Cart(quantity=%s)' % (self.quantity,)

    def __iter__(self):
        return iter(self.lines.all())

    def __len__(self):
        return self.lines.count()

    def order_cart(self):
        self.is_ordered = True
        self.token = binascii.hexlify(os.urandom(20)).decode()
class CartLine(models.Model):
    cart = models.ForeignKey(
        Cart, related_name='lines', on_delete=models.CASCADE)
    event = models.ForeignKey(
        'event.Event', related_name='event_carts', on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(default=0, null=True, blank=True)
    data = JSONField(blank=True, default=dict)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return "id:{}---event:{}--gift:{}".format(self.id, self.event.id, self.is_gift)