from django.utils import timezone
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from app.models import Book


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
