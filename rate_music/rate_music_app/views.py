from django.shortcuts import render
from django.http import Http404

from rate_music.rate_music_app.models import Band, Album


def home(request):
    bands = Band.objects.all()
    return render(request, 'home.html', {
        'bands': bands,
    })


def band_detail(request, band_name_link):
    try:
        band = Band.objects.get(name=band_name_link)
        band_id = band.id
        albums = Album.objects.filter(band=band_id)
    except Band.DoesNotExist:
        raise Http404('Band not found')

    return render(request, 'band_detail.html', {
        'band': band,
        'albums': albums,
    })
