from django.contrib.auth.models import User
from django.db import models

from django.urls import reverse


class CommonInfo(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Language(CommonInfo):
    language = models.CharField(max_length=64)

    def get_absolute_url(self):
        return reverse('language', args=[str(self.id)])

    def __str__(self):
        return "Language {}".format(self.id)


class Genre(CommonInfo):
    genre = models.CharField(max_length=64)

    def get_absolute_url(self):
        return reverse('genre', args=[str(self.id)])

    def __str__(self):
        return "Genre {}".format(self.id)


class Book(CommonInfo):
    name = models.CharField(max_length=64)
    summary = models.CharField(max_length=255)
    genre = models.ManyToManyField(Genre, related_name="books")
    language = models.ManyToManyField(Language, related_name="books")

    def get_absolute_url(self):
        return reverse('book', args=[str(self.id)])

    def __str__(self):
        return "Book {}".format(self.id)


class Author(CommonInfo):
    name = models.CharField(max_length=64)
    birth_date = models.DateField(blank=True)
    death_date = models.DateField(blank=True)
    nationality = models.CharField(max_length=64,blank=True)
    birth_place = models.CharField(max_length=64, blank=True)
    books = models.ManyToManyField(Book, related_name="authors")

    def get_absolute_url(self):
        return reverse('author', args=[str(self.id)])

    def __str__(self):
        return "Author {}".format(self.id)


class BookInstance(CommonInfo):
    status_choices = (
        ('M', 'Maintenance')
        , ('L', 'On Loan')
        , ('A', 'Available')
        , ('R', 'Reserved')
    )

    due_book_date = models.DateField()
    status = models.CharField(max_length=1, choices=status_choices)
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, related_name="instance", null=True)
    person = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="persons_assign_to_book", null=True)

    def get_absolute_url(self):
        return reverse('book_instance.details', args=[str(self.id)])

    def __str__(self):
        return "BookInstance {}".format(self.id)
