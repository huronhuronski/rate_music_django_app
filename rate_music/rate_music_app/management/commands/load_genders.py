from django.core.management.base import BaseCommand

from rate_music.rate_music_app.models import Gender


GENDER_LIST = [
    'Black', 'Death', 'Sludge', 'Doom', 'Post',
    'Heavy', 'Melodic', 'Folk', 'Industrial', 'Experimental',
    'Thrash', 'Groove', 'Grindcore', 'Hardcore', 'Deathcore',
    'Math', 'Noise', 'Drone', 'War', 'Shoegaze'
]


class Command(BaseCommand):
    def handle(self, *args, **options):
        for gender_item in GENDER_LIST:
            Gender.objects.create(gender=gender_item)
