from django.contrib import admin
from django.urls import path

from .views.author import AuthorPageView, AuthorsPageView, CreateAuthorView
from .views.book import BooksPageView, BookPageView, CreateBookView
from .views.home import HomePageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalog/', HomePageView.as_view(), name="home"),
    path('catalog/books/', BooksPageView.as_view(), name="books"),
    path('catalog/book/<int:pk>/', BookPageView.as_view(), name='book'),
    path('catalog/book/add/', CreateBookView.as_view(), name='add book'),
    path('catalog/authors/', AuthorsPageView.as_view(), name="authors"),
    path('catalog/author/<int:pk>/', AuthorPageView.as_view(), name='author'),
    path('catalog/author/add/', CreateAuthorView.as_view(), name='add author'),
]
