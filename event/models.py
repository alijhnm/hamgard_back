from django.db import models


class EventCategory(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Event(models.Model):
    vendor = models.ForeignKey("account.Vendor", on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    address = models.ForeignKey("Address", on_delete=models.CASCADE, blank=True)
    category = models.ForeignKey(EventCategory, on_delete=models.CASCADE)
    summary = models.TextField(blank=True, null=True)
    discount = models.FloatField(null=True, blank=True)
    price = models.FloatField()
    tags = models.ManyToManyField('Tag', blank=True)


    def __str__(self):
        return self.title


class EventImage(models.Model):
    Event = models.ForeignKey(Event, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="event_images")
    alt = models.CharField(max_length=100)

    def __str__(self):
        return self.alt


class EventVideo(models.Model):
    Event = models.OneToOneField(Event, related_name="video", on_delete=models.CASCADE)
    video = models.FileField()
    alt = models.CharField(max_length=100)

    def __str__(self):
        return str(self.pk)


class Province(models.Model):
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name


class City(models.Model):
    province = models.ForeignKey(Province, related_name="cities", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=50, null=True, blank=True)
    lat = models.FloatField(null=True, blank=True, default=None)
    lng = models.FloatField(null=True, blank=True, default=None)

    def __str__(self):
        return self.name


class Address(models.Model):
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    address_text = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return str(self.pk)


class PlaceCategory(models.Model):
    name_fa = models.CharField(max_length=500)
    name_en = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name_fa


class Tag(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name


class Place(models.Model):
    name_fa = models.CharField(max_length=500, null=True, blank=True)
    name_en = models.CharField(max_length=500, null=True, blank=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag', blank=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    category = models.ForeignKey(PlaceCategory, on_delete=models.CASCADE, null=True, blank=True)
    # image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return "id:{}, name:{}".format(self.id, self.name_en)


class PlaceImage(models.Model):
    place = models.ForeignKey(Place, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="place_images")
    alt = models.CharField(max_length=100)

    def __str__(self):
        return self.alt