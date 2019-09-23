from django.utils import timezone
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from app.models import Author


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
