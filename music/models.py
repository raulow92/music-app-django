from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    image_url = models.CharField(max_length=200, default='https://community.spotify.com/t5/image/serverpage/image-id/55829iC2AD64ADB887E2A5?v=v2')

    def __str__(self):
        return self.name

class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    pub_date = models.DateField('date published')

    def __str__(self):
        return f"{self.artist} - {self.name}"