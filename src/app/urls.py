from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("something/", views.something, name="something"),
    path("listing/", views.listing, name="listing"),
    path("filter-list/", views.filter_list, name="filter-list"),
    # path("books-by-date/", views.books_by_date, name="books-by-date"),
    path("books-by-date/", views.BooksByDateView.as_view(), name="books-by-date"),
    path("books-card-list/", views.books_card_list, name="books-card-list"),
]