from django.contrib import admin
from django.urls import path

from .views.BookInstance import (CreateBookInstanceView,
                                 BookInstancePageView, BookInstancesPageView)
from .views.author import (AuthorPageView, AuthorsPageView, CreateAuthorView)
from .views.book import (BooksPageView, BookPageView, CreateBookView)
from .views.genre import (GenrePageView, GenresPageView, CreateGenreView)
from .views.home import HomePageView
from .views.language import (LanguagePageView,
                             LanguagesPageView, CreateLanguageView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalog/', HomePageView.as_view(), name="home"),
    path('catalog/books/', BooksPageView.as_view(), name="books"),
    path('catalog/book/<int:pk>/', BookPageView.as_view(), name='book'),
    path('catalog/book/add/', CreateBookView.as_view(), name='add book'),

    path('catalog/authors/', AuthorsPageView.as_view(), name="authors"),
    path('catalog/author/<int:pk>/', AuthorPageView.as_view(), name='author'),
    path('catalog/author/add/',
         CreateAuthorView.as_view(), name='add author'),

    path('catalog/genres/', GenresPageView.as_view(), name="genres"),
    path('catalog/genre/<int:pk>/', GenrePageView.as_view(), name='genre'),
    path('catalog/genre/add/', CreateGenreView.as_view(), name='add genre'),

    path('catalog/languages/',
         LanguagesPageView.as_view(), name="languages"),
    path('catalog/language/<int:pk>/',
         LanguagePageView.as_view(), name='language'),
    path('catalog/language/add/',
         CreateLanguageView.as_view(), name='add language'),

    path('catalog/book-instances/',
         BookInstancesPageView.as_view(), name="book-instances"),
    path('catalog/book-instance/<int:pk>/',
         BookInstancePageView.as_view(), name='book-instance'),
    path('catalog/book-instance/add/',
         CreateBookInstanceView.as_view(), name='add book-instance'),
]
