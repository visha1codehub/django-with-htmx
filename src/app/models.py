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

    # class Meta:
    #     ordering = ['-publication_date']
