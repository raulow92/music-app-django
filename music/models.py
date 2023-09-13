from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    pub_date = models.DateField('date published')

    def __str__(self):
        return f"{self.artist} - {self.name}"