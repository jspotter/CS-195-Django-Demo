from django.http import HttpResponse
from django.template import loader

from . import models, forms

def add_genre(genre_to_add):
    matching_genres = models.MusicGenre.objects.filter(genre=genre_to_add)

    if len(matching_genres) == 0:
        new_genre = models.MusicGenre(genre=genre_to_add, count=1)
        new_genre.save()
    else:
        matching_genres[0].count += 1
        matching_genres[0].save()

def add_artist(artist_to_add, genre_id):
    matching_artists = models.Artist.objects.filter(name=artist_to_add, genre=genre_id)

    if len(matching_artists) == 0:
        associated_genre = models.MusicGenre.objects.get(pk=genre_id)

        new_artist = models.Artist(name=artist_to_add, genre=associated_genre, count=1)
        new_artist.save()
    else:
        matching_artists[0].count += 1
        matching_artists[0].save()

def home(request):

    if request.method == 'POST':
        genre_form = forms.GenreForm(request.POST)

        if genre_form.is_valid():
            genre_to_add = genre_form.cleaned_data['genre']
            add_genre(genre_to_add)

    template = loader.get_template('home.html')

    existing_genres = models.MusicGenre.objects.all()

    form = forms.GenreForm()

    return HttpResponse(template.render(\
        {
            'genres': existing_genres,
            'form': form
        },
        request))

def genre_page(request, genre_id):

    if request.method == 'POST':
        artist_form = forms.ArtistForm(request.POST)

        if artist_form.is_valid():
            artist_to_add = artist_form.cleaned_data['artist']
            
            associated_genre = artist_form.cleaned_data['genre']

            add_artist(artist_to_add, associated_genre)

    template = loader.get_template('genre.html')
    
    artists = models.Artist.objects.filter(genre__pk=genre_id)

    genre = models.MusicGenre.objects.get(pk=genre_id)

    form = forms.ArtistForm({'genre': genre_id})

    return HttpResponse(template.render(\
        {
            'genre': genre,
            'artists': artists,
            'form': form
        },
        request))