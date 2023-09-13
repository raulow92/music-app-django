from django.shortcuts import render
from django.http import HttpResponse
from music.forms import ArtistForm
from music.models import Artist


def index(request):
    artists = Artist.objects.all()
    context = {'artists': artists}
    return render(request, 'music/index.html', context)

def artist_detail(request, artist_id):
    artist = Artist.objects.get(id=artist_id)
    if request.method == 'POST':
        form = ArtistForm(request.POST, instance=artist)
        if form.is_valid():
            artist = form.save()
    else:
        form = ArtistForm(instance=artist)
    context = {'artist': artist, 'form': form}
    return render(request, 'music/artist_detail.html', context)