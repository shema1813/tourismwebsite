from django.db import models

# Create your models here.
class player (models.Model) :
    username = models.CharField(max_length = 20 )
    password = models.CharField (max_length=20)
    profile_pic = models.ImageField()

class Resource (models.Model) :
    name = models.CharField (max_length=6)
    points = models.IntegerField ()

class Movie(models.Model) : 
    name = models.CharField (max_length=6)
    description = models.TextField()
