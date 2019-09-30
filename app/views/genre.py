from django import forms
from django.http.response import HttpResponseRedirect
from django.views.generic.edit import CreateView

from app.models import Language


class LanguageForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = ("__all__")

    def save(self, commit=True):
        self.instance.save()
        return self.instance


class CreateAuthorView(CreateView):
    model = Language
    form_class = LanguageForm
    template_name = 'app/create.html'
    success_url = '/catalog'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        return HttpResponseRedirect(self.get_success_url())
