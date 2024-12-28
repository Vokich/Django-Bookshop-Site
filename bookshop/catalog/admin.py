from django.contrib import admin
from .models import Author, Book, BookInstance, Genre, Language, Status
# Register your models here.

#admin.site.register(Author)
#admin.site.register(Book)
#admin.site.register(BookInstance)
admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Status)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')

admin.site.register(Author, AuthorAdmin)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'language', 'display_author')
    list_filter = ('genre', 'author')

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'book')



