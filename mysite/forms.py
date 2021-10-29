from django import forms

class GenreForm(forms.Form):
    genre = forms.CharField(label='Favorite Music Genre', max_length=200)

class ArtistForm(forms.Form):
    artist = forms.CharField(label='Artist Name', max_length=200)
    genre = forms.IntegerField(widget = forms.HiddenInput())