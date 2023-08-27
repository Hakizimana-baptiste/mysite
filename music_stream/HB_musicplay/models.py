from django.db import models
from django.contrib.auth.models import User

# class User(models.Model):
#     username = models.CharField(max_length=100)
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=100)
#     role = models.CharField(max_length=20)
#
#     def __str__(self):
#         return self.username


class Artist(models.Model):
    name = models.CharField(max_length=20,blank=False)
    age = models.BigIntegerField()
    sex = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Song(models.Model):
    arist = models.ForeignKey(Artist,default= None,on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=100)
    duration = models.PositiveIntegerField()
    release_date = models.DateField()
    genre = models.CharField(max_length=50)
    audio = models.FileField(upload_to='Songs/', blank=True)

    def __str__(self):
        return self.title


class Playlist(models.Model):
    name = models.CharField(max_length=200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    songs = models.ManyToManyField(Song)

    def __str__(self):
        return self.name
