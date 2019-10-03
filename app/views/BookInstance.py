from django import forms
from django.http.response import HttpResponseRedirect
from django.utils import timezone
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from app.models import BookInstance


class BookInstanceForm(forms.ModelForm):
    class Meta:
        model = BookInstance
        fields = ("__all__")

    def save(self, commit=True):
        self.instance.save()
        return self.instance


class CreateBookInstanceView(CreateView):
    model = BookInstance
    form_class = BookInstanceForm
    template_name = 'app/create.html'
    success_url = '/catalog/book-instances/'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        return HttpResponseRedirect(self.get_success_url())


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
