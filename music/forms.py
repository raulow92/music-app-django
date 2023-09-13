from django import forms
from music.models import Artist

class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = "__all__"