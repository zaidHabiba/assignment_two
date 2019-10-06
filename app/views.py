from django.utils import timezone
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView
from django.views.generic.list import ListView

from app.forms import (AuthorForm, BookInstanceForm,
                       BookForm, GenreForm, LanguageForm)
from app.models import (Author, BookInstance,
                        Genre, Language, Book)


class HomePageView(TemplateView):
    template_name = "app/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Book.objects.all()
        context['instance'] = BookInstance.objects.all()
        context['author'] = Author.objects.all()
        context['instance_available'] = BookInstance.objects.filter(status="A")
        return context


class CreateAuthorView(FormView):
    form_class = AuthorForm
    template_name = 'app/create.html'
    success_url = '/catalog/authors/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class AuthorsPageView(ListView):
    template_name = "app/authors.html"
    model = Author

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class AuthorPageView(DetailView):
    template_name = "app/author.html"
    model = Author

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class CreateBookView(FormView):
    form_class = BookForm
    template_name = 'app/create.html'
    success_url = '/catalog/books/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class BooksPageView(ListView):
    template_name = "app/books.html"
    model = Book

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class BookPageView(DetailView):
    template_name = "app/book.html"
    model = Book

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class CreateBookInstanceView(FormView):
    form_class = BookInstanceForm
    template_name = 'app/create.html'
    success_url = '/catalog/book-instances/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class BookInstancesPageView(ListView):
    template_name = "app/book-instances.html"
    model = BookInstance

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class BookInstancePageView(DetailView):
    template_name = "app/book-instance.html"
    model = BookInstance

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class CreateGenreView(FormView):
    form_class = GenreForm
    template_name = 'app/create.html'
    success_url = '/catalog/genres/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class GenresPageView(ListView):
    template_name = "app/genres.html"
    model = Genre

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class GenrePageView(DetailView):
    template_name = "app/genre.html"
    model = Genre

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class CreateLanguageView(FormView):
    form_class = LanguageForm
    template_name = 'app/create.html'
    success_url = '/catalog/languages/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class LanguagesPageView(ListView):
    template_name = "app/languages.html"
    model = Language

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class LanguagePageView(DetailView):
    template_name = "app/language.html"
    model = Language

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
