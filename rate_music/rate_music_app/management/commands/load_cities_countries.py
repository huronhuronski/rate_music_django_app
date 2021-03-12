from csv import DictReader

from django.core.management.base import BaseCommand

from rate_music.rate_music_app.models import GeoCountry, GeoCity


class Command(BaseCommand):
    def handle(self, *args, **options):
        for row in DictReader(open('./worldcities.csv', 'r', encoding='utf-8')):
            GeoCountry.objects.update_or_create(country=row['country'],
                                                iso2=row['iso2'],
                                                iso3=row['iso3'])
            GeoCity.objects.create(city=row['city'],
                                   city_ascii=row['city_ascii'],
                                   lat=float(row['lat']),
                                   lng=float(row['lng']),
                                   country=GeoCountry.objects.get(country=row['country']))
