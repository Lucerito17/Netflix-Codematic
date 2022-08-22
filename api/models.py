from pyexpat import model
from unicodedata import name
from django.db import models

class Actor(models.Model):
    name=models.CharField(max_length=255,null=False)
    def __str__(self):
        return self.name

class Gender(models.Model):
    name=models.CharField(max_length=255, null=False)
    def __str__(self):
        return self.name

class Movie(models.Model):
    name = models.CharField(max_length=255, null=True)
    poster = models.ImageField(upload_to='posters', null=True)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE, null=True)
    actor = models.ManyToManyField(Actor)
    def __str__(self):
        return self.name