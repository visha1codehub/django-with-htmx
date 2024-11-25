from django.contrib import admin
from .models import Book, Section, Chapter, Notification


class BookAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "author", "pages", "publication_date", "language")

class NotificationAdmin(admin.ModelAdmin):
    list_display = ("id", "content_type", "object_id", "content_object", "text", "created_at")


admin.site.register(Book, BookAdmin)
admin.site.register(Section)
admin.site.register(Chapter)
admin.site.register(Notification, NotificationAdmin)
