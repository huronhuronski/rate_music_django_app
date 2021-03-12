from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

from datetime import date
from dateutil.relativedelta import relativedelta


class Album(models.Model):
    title = models.CharField(max_length=100)
    band = models.ForeignKey('Band', on_delete=models.CASCADE)
    band_split = models.ForeignKey('Band',
                                   null=True,
                                   blank=True,
                                   on_delete=models.SET_NULL,
                                   related_name='split_second_band')
    date_released = models.DateField(null=True, blank=True)
    cover = models.ImageField(null=True, blank=True)
    label = models.ForeignKey('Label', null=True, blank=True, on_delete=models.SET('unknown'))

    def __str__(self):
        return self.title


class Band(models.Model):
    name = models.CharField(max_length=100)
    date_formed = models.DateField(null=True, blank=True)
    active = models.BooleanField(default=True)
    gender = models.ManyToManyField('Gender')
    label_current = models.ForeignKey('Label', on_delete=models.SET('unknown'), null=True, blank=True)
    labels_past = models.ManyToManyField('Label',
                                         blank=True,
                                         related_name='band_past_labels')
    country = models.ForeignKey('GeoCountry', on_delete=models.SET('unknown'))
    city = models.ForeignKey('GeoCity', on_delete=models.SET('unknown'), null=True, blank=True)
    links = models.CharField(max_length=100, null=True, blank=True)
    band_logo = models.ImageField(null=True, blank=True)
    band_photo = models.ImageField(null=True, blank=True)

    name_link = str(name).replace(' ', '%20')

    def years_active(self):
        difference = relativedelta(date.today(), self.date_formed)
        return difference.years

    def __str__(self):
        return self.name


class Label(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100, null=True, blank=True)
    country = models.ForeignKey('GeoCountry', on_delete=models.SET('unknown'))
    active = models.BooleanField(default=True)
    website = models.URLField(null=True, blank=True)
    webshop = models.URLField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.name


class Rating(models.Model):
    album = models.ForeignKey('Album', on_delete=models.CASCADE)
    value = models.IntegerField(default=5,
                                validators=[
                                    MaxValueValidator(10),
                                    MinValueValidator(0)
                                ])
    datetime_rating = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.SET('unknown[`]'))
    review_title = models.CharField(max_length=250, null=True, blank=True)
    review_content = models.TextField(null=True, blank=True)

    def __str__(self):
        album_rating = str(self.album) + ': ' + str(self.value)
        return album_rating


class Gender(models.Model):
    gender = models.CharField(max_length=50)

    def __str__(self):
        return self.gender


class GeoCity(models.Model):
    city = models.CharField(max_length=100)
    city_ascii = models.CharField(max_length=100)
    lat = models.DecimalField(max_digits=13, decimal_places=10)
    lng = models.DecimalField(max_digits=13, decimal_places=10)
    country = models.ForeignKey('GeoCountry', on_delete=models.CASCADE)

    def coordinates(self):
        return str(self.lat) + str(self.lng)

    def __str__(self):
        return self.city_ascii


class GeoCountry(models.Model):
    country = models.CharField(max_length=100)
    iso2 = models.CharField(max_length=2)
    iso3 = models.CharField(max_length=3)

    def __str__(self):
        return self.country
