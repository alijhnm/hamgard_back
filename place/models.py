from django.db import models


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
    lat = models.FloatField(null=True, blank=True)
    lng = models.FloatField(null=True, blank=True)
    address_text = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.address_text


class PlaceCategory(models.Model):
    name_fa = models.CharField(max_length=500)
    name_en = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name_fa


class Place(models.Model):
    name_fa = models.CharField(max_length=500)
    name_en = models.CharField(max_length=500, null=True, blank=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    category = models.ForeignKey(PlaceCategory, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name_fa
