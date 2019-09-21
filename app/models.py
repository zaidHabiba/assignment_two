from django.contrib.auth.models import User
from django.db import models


class Language(models.Model):
    language = models.CharField(max_length=64)


class Genre(models.Model):
    genre = models.CharField(max_length=64)


class Author(models.Model):
    name = models.TextField(max_length=64)
    birth_date = models.DateField()
    death_date = models.DateField(blank=True, null=True)
    nationality = models.TextField()
    birth_place = models.TextField(blank=True, null=True)


class Book(models.Model):
    name = models.TextField()
    authors = models.ForeignKey(Author, on_delete=models.DO_NOTHING)
    summary = models.TextField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)


class BookInstance(models.Model):
    status_choices = {
        'Maintenance': 'M'
        , 'On Loan': 'L'
        , 'Available': 'A'
        , 'Reserved': 'R'
    }
    due_book_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=1, choices=status_choices)
    book = models.ForeignKey(Book, on_delete=models.DO_NOTHING)
    person = models.ForeignKey(User, on_delete=models.DO_NOTHING)
