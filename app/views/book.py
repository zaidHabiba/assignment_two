from django import forms
from django.utils import timezone
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView
from django.views.generic.list import ListView

from app.models import Book
from django import forms
from django.http.response import HttpResponseRedirect
from django.utils import timezone
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ("__all__")

    def save(self, commit=True):
        self.instance.save()
        return self.instance


class CreateBookView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'app/create.html'
    success_url = '/catalog/books/'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        return HttpResponseRedirect(self.get_success_url())

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
