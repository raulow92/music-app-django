from django.shortcuts import render
from django.http import HttpResponse
from music.forms import ArtistForm, AlbumForm, ImportForm
from music.models import Artist, Album
import requests

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

def album_detail(request, album_id):
    album = Album.objects.get(id=album_id)
    if request.method == 'POST':
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            album = form.save()
    else:
        form = AlbumForm(instance=album)

    context = {'album': album, 'form': form}
    return render(request, 'music/album_detail.html', context)

def artist_import(request):
    artist_data = None
    if request.method == 'POST':
        form = ImportForm(request.POST)
        if form.is_valid():
            artist_id = form.cleaned_data['artist_id']
            url = f"https://api.discogs.com/artists/{artist_id}" 
            artist_data = requests.get(url).json()
            if form.cleaned_data['import_artist']:
                Artist.objects.create(name=artist_data['name'], genre="No disponible")
        print("hola")
    else:
        form = ImportForm()
    context = {'form': form, 'artist': artist_data}
    return render(request, 'music/artist_import.html', context)