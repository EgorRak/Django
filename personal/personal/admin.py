from django.contrib import admin
from .models import Author, Country, Book, Genre, BookCopy, Reader, Order, Librarian
from import_export import resources
from import_export.admin import ImportExportActionModelAdmin

class BookResource(resources.ModelResource):

    class Meta:
        model = Book


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass
@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    pass
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass
@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass
@admin.register(BookCopy)
class BookCopyAdmin(admin.ModelAdmin):
    pass
@admin.register(Reader)
class ReaderAdmin(admin.ModelAdmin):
    pass
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass
@admin.register(Librarian)
class LibrarianAdmin(admin.ModelAdmin):
    pass

