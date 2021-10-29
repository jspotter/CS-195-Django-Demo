from django.db import models

class MusicGenre(models.Model):
    genre = models.CharField(max_length=200)
    count = models.IntegerField()

    def __str__(self):
        return '{} ({})'.format(self.genre, self.count)

class Artist(models.Model):
    name = models.CharField(max_length=200)
    count = models.IntegerField()
    genre = models.ForeignKey(MusicGenre, on_delete=models.CASCADE)

    def __str__(self):
        return '{} ({})'.format(self.name, self.count)