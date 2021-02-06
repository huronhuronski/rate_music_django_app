from django.db import models

from datetime import date

GENDERS = [
    ('bl', 'black'),
    ('de', 'death'),
    ('sl', 'sludge'),
    ('do', 'doom'),
    ('hv', 'heavy'),
]


class Album(models.Model):
    title = models.CharField(max_length=300)
    band = models.ForeignKey('Band', on_delete=models.SET_NULL)
    rating = models.DecimalField(decimal_places=1)
    date_released = models.DateField()
    cover = models.ImageField()
    label = models.ForeignKey('Label', on_delete=models.SET_NULL)


class Band(models.Model):
    name = models.CharField(max_length=200)
    date_formed = models.DateField()
    year_active = date.today() - date_formed
    active = models.BooleanField()
    gender = models.CharField()
    label_current = models.ForeignKey('Label', on_delete=models.SET_NULL)
    labels_past = models.CharField()
    country = models.CharField()
    location = models.CharField()
    links = models.CharField()


class Rating(models.Model):
    album = models.ForeignKey('Album', on_delete=models.SET_NULL)
    value = models.IntegerField()
    date_rate = models.DateTimeField()


class Label(models.Model):
    name = models.CharField()
    address = models.CharField()
    country = models.CharField()
    active = models.BooleanField()
    website = models.URLField()
    webshop = models.URLField()
    email = models.EmailField()
    label_gender = models.CharField(
        max_length=2,
        choices=GENDERS,
        default=models.SET_NULL
    )
