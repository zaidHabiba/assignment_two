from django.views.generic.base import TemplateView

from app.models import (Book, BookInstance, Author)


class HomePageView(TemplateView):
    template_name = "app/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Book.objects.all()
        context['instance'] = BookInstance.objects.all()
        context['author'] = Author.objects.all()
        context['instance_available'] = BookInstance.objects.filter(status="A")
        return context
