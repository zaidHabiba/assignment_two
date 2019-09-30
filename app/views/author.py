from django import forms
from django.http.response import HttpResponseRedirect
from django.utils import timezone
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from app.models import Author


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ("__all__")

    def save(self, commit=True):
        self.instance.save()
        return self.instance


class CreateAuthorView(CreateView):
    model = Author
    form_class = AuthorForm
    template_name = 'app/create.html'
    success_url = '/catalog/authors/'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        return HttpResponseRedirect(self.get_success_url())


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
