from django import forms

from app.models import Author, BookInstance, Genre, Language, Book


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ("__all__")

    def save(self, commit=True):
        self.instance.save()
        return self.instance


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ("__all__")

    def save(self, commit=True):
        self.instance.save()
        return self.instance


class BookInstanceForm(forms.ModelForm):
    class Meta:
        model = BookInstance
        fields = ("__all__")

    def save(self, commit=True):
        self.instance.save()
        return self.instance


class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ("__all__")

    def save(self, commit=True):
        self.instance.save()
        return self.instance


class LanguageForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = ("__all__")

    def save(self, commit=True):
        self.instance.save()
        return self.instance
