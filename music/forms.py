from django import forms
from music.models import Artist, Album

class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = "__all__"

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = "__all__"