from django.db import models
from django.utils import timezone


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_date = models.DateField(default=timezone.now)
    pages = models.IntegerField()
    language = models.CharField(max_length=50, default="English")
    front_page = models.ImageField(
        upload_to="book_front_pages/",
        blank=True,
        null=True,
        default="book_front_pages/default.jpeg",
    )


    def save(self, *args, **kwargs):
        if not self.front_page:
            self.front_page = "book_front_pages/default.jpeg"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']

class Section(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.book.title + "-" + self.title


class Chapter(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.section.book.title + "-" + self.section.title + "-" + self.title


from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class Notification(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveSmallIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.text