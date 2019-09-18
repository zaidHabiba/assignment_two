from django.db import models

class Language(models.Model):
    language = models.CharField(max_length=64)

class Genre(models.Model):
    genre = models.CharField(max_length=64)

class Book(models.Model):
    name = models.CharField(max_length=64)
    author = models.CharField(max_length=64)
    summary = models.CharField(max_length=255)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)


