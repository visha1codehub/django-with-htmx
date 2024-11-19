from django.contrib import admin
from .models import Book, Section, Chapter


class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "pages", "publication_date", "language")


admin.site.register(Book, BookAdmin)
admin.site.register(Section)
admin.site.register(Chapter)
