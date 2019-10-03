from django import forms
from django.http.response import HttpResponseRedirect
from django.utils import timezone
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from app.models import Genre


class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ("__all__")

    def save(self, commit=True):
        self.instance.save()
        return self.instance


class CreateGenreView(CreateView):
    model = Genre
    form_class = GenreForm
    template_name = 'app/create.html'
    success_url = '/catalog/genres/'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        return HttpResponseRedirect(self.get_success_url())


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
