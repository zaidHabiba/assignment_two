from django.contrib import admin
from django.contrib.auth.models import Permission, Group

from .models import Book, Genre, Language, BookInstance, Author

admin.site.register(Permission)


class BookInstanceInline(admin.TabularInline):
    model = BookInstance


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'summary', 'genre_list',)
    list_filter = ('id', 'name', 'summary',)
    fieldsets = (
        (None, {
            'fields': ('name', 'summary',)
        }),
        ('Languages and Genre options', {
            'classes': ('collapse',),
            'fields': ('language', 'genre',),
        }),
    )
    inlines = [
        BookInstanceInline,
    ]

    def genre_list(self, obj):
        return ", ".join([genre_item.genre for genre_item in obj.genre.all()])


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'due_book_date', 'status', 'book', 'person',)
    list_filter = ('due_book_date', 'status', 'book', 'person',)
    fieldsets = (
        (None, {
            'fields': ('status', 'book',)
        }),
        ('Person options', {
            'classes': ('collapse',),
            'fields': ('person',),
        }),
    )


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'birth_date', 'death_date',
                    'nationality', 'birth_place',)
    list_filter = ('name', 'birth_date', 'death_date',
                   'nationality', 'birth_place',)


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'genre',)
    list_filter = ('genre',)


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('id', 'language',)
    list_filter = ('language',)
