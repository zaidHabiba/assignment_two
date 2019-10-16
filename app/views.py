from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import Group
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeForm
from django.shortcuts import redirect
from django.utils import timezone
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView
from django.views.generic.list import ListView

from app.forms import (AuthorForm, BookInstanceForm,
                       BookForm, GenreForm, LanguageForm)
from app.models import (Author, BookInstance,
                        Genre, Language, Book)

LOGIN_URL = "/catalog/login/"


class HomePageView(LoginRequiredMixin, TemplateView):
    template_name = "app/index.html"
    login_url = LOGIN_URL

    def get_context_data(self, **kwargs):
        print(self.request)
        context = super().get_context_data(**kwargs)
        context['books'] = Book.objects.all()
        context['instance'] = BookInstance.objects.all()
        context['author'] = Author.objects.all()
        context['instance_available'] = BookInstance.objects.filter(status="A")
        return context


class CreateAuthorView(PermissionRequiredMixin, LoginRequiredMixin, FormView):
    form_class = AuthorForm
    template_name = 'app/create.html'
    success_url = '/catalog/authors/'
    login_url = LOGIN_URL
    permission_required = 'app.add_author'

    def form_valid(self, form):
        form_valid = super().form_valid(form)
        form.save()
        return form_valid


class AuthorsPageView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    template_name = "app/authors.html"
    model = Author
    login_url = LOGIN_URL
    permission_required = 'app.view_author'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class AuthorPageView(PermissionRequiredMixin, LoginRequiredMixin, DetailView):
    template_name = "app/author.html"
    model = Author
    login_url = LOGIN_URL
    permission_required = 'app.view_author'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class CreateBookView(PermissionRequiredMixin, LoginRequiredMixin, FormView):
    form_class = BookForm
    template_name = 'app/create.html'
    success_url = '/catalog/books/'
    login_url = LOGIN_URL
    permission_required = 'app.add_book'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class BooksPageView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    template_name = "app/books.html"
    model = Book
    login_url = LOGIN_URL
    permission_required = 'app.view_book'

    def get_context_data(self, **kwargs):
        search_value = self.request.GET.get("search", "")
        if search_value is not "":
            books = Book.objects.filter(name__contains=search_value)
            return {"object_list": books}
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class BookPageView(PermissionRequiredMixin, LoginRequiredMixin, DetailView):
    template_name = "app/book.html"
    model = Book
    login_url = LOGIN_URL
    permission_required = 'app.view_book'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class CreateBookInstanceView(PermissionRequiredMixin, LoginRequiredMixin, FormView):
    form_class = BookInstanceForm
    template_name = 'app/create.html'
    success_url = '/catalog/book-instances/'
    login_url = LOGIN_URL
    permission_required = 'app.add_bookinstance'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class BookInstancesPageView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    template_name = "app/book-instances.html"
    model = BookInstance
    login_url = LOGIN_URL
    permission_required = 'app.view_bookinstance'

    def get_context_data(self, **kwargs):
        if self.request.user.is_superuser:
            context = {"object_list": BookInstance.objects.all()}
        else:
            context = {"object_list": BookInstance.objects.filter(person=self.request.user)}
        return context


class BookInstancePageView(PermissionRequiredMixin, LoginRequiredMixin, DetailView):
    template_name = "app/book-instance.html"
    model = BookInstance
    login_url = LOGIN_URL
    permission_required = 'app.view_bookinstance'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class CreateGenreView(PermissionRequiredMixin, LoginRequiredMixin, FormView):
    form_class = GenreForm
    template_name = 'app/create.html'
    success_url = '/catalog/genres/'
    login_url = LOGIN_URL
    permission_required = 'app.add_genre'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class GenresPageView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    template_name = "app/genres.html"
    model = Genre
    login_url = LOGIN_URL
    permission_required = 'app.view_genre'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class GenrePageView(PermissionRequiredMixin, LoginRequiredMixin, DetailView):
    template_name = "app/genre.html"
    model = Genre
    login_url = LOGIN_URL
    permission_required = 'app.view_genre'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class CreateLanguageView(PermissionRequiredMixin, LoginRequiredMixin, FormView):
    form_class = LanguageForm
    template_name = 'app/create.html'
    success_url = '/catalog/languages/'
    login_url = LOGIN_URL
    permission_required = 'app.add_language'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class LanguagesPageView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    template_name = "app/languages.html"
    model = Language
    login_url = LOGIN_URL
    permission_required = 'app.view_language'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class LanguagePageView(PermissionRequiredMixin, LoginRequiredMixin, DetailView):
    template_name = "app/language.html"
    model = Language
    login_url = LOGIN_URL
    permission_required = 'app.view_language'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class LoginPageView(LoginView):
    template_name = 'app/login.html'
    success_url = '/catalog'
    login_url = LOGIN_URL

    def form_valid(self, form):
        username = form.data["username"]
        password = form.data["password"]
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        else:
            return redirect("/catalog/login/")

    def get_redirect_url(self):
        return "/catalog"


class LogoutPageView(LogoutView):

    def post(self, request, *args, **kwargs):
        logout(request)
        return redirect("/catalog/login/")

    def get_redirect_url(self):
        return "/catalog/login/"


class ChangePassword(PasswordChangeView):
    template_name = 'admin/change_form.html'
    success_url = '/catalog'
    form_class = PasswordChangeForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class Signup(FormView):
    template_name = 'app/signup.html'
    success_url = '/catalog'
    form_class = UserCreationForm

    def form_valid(self, form):
        form_valid = super().form_valid(form)
        user = form.save()
        group = Group.objects.get(name='User')
        print(user.groups.add(group))
        return form_valid
