from django.contrib.auth.models import User
from django.db import models

from django.urls import reverse


class Language(models.Model):
    language = models.CharField(max_length=64)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True, blank=True)

    def get_absolute_url(self):
        return reverse('language', args=[str(self.id)])

    def __str__(self):
        return "Language {}".format(self.id)


class Genre(models.Model):
    genre = models.CharField(max_length=64)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True, blank=True)

    def get_absolute_url(self):
        return reverse('genre', args=[str(self.id)])

    def __str__(self):
        return "Genre {}".format(self.id)


class Book(models.Model):
    name = models.TextField()
    summary = models.TextField(blank=True)
    genre = models.ManyToManyField(Genre, related_name="books")
    language = models.ManyToManyField(Language, related_name="books")
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True, blank=True)

    def get_absolute_url(self):
        return reverse('book', args=[str(self.id)])

    def __str__(self):
        return "Book {}".format(self.id)


class Author(models.Model):
    name = models.TextField(max_length=64)
    birth_date = models.DateField()
    death_date = models.DateField(blank=True, null=True)
    nationality = models.TextField()
    birth_place = models.TextField(blank=True, null=True)
    books = models.ManyToManyField(Book, related_name="authors")
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True, blank=True)

    def get_absolute_url(self):
        return reverse('author', args=[str(self.id)])

    def __str__(self):
        return "Author {}".format(self.id)


class BookInstance(models.Model):
    status_choices = (
        ('M', 'Maintenance')
        , ('L', 'On Loan')
        , ('A', 'Available')
        , ('R', 'Reserved')
    )

    due_book_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=1, choices=status_choices)
    book = models.ForeignKey(Book, on_delete=models.DO_NOTHING, related_name="instance")
    person = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="persons_assign_to_book")
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True, blank=True)

    def get_absolute_url(self):
        return reverse('book_instance.details', args=[str(self.id)])

    def __str__(self):
        return "BookInstance {}".format(self.id)
