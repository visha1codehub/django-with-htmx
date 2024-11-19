from django.shortcuts import render
import random
from datetime import datetime
from django.db.models import Q
from .models import Book, Section, Chapter
from icecream import ic as iprint


def index(request):
    x = random.randint(1, 1000)
    books = Book.objects.all()
    # iprint(type(books), books)
    for book in books:
        book.chapters = Chapter.objects.filter(section__book=book).count()
    # iprint(type(books), books)

    return render(request, "index.html", {"x": x, "books": books})


def something(request):
    date = request.GET.get("date")
    x = random.randint(1, 1000)
    if not date:
        date = datetime.today().strftime("%Y-%m-%d")

    return render(request, "partials/something.html", {"x": x, "date": date})


random_list = sorted([random.randint(1, 1100) for _ in range(80)])


def listing(request):
    iprint(request.headers.get("HX-Request"))
    return render(request, "listing.html", {"lst": random_list})


def filter_list(request):
    iprint(request.headers.get("HX-Request"))
    num = request.GET.get("num").strip()
    try:
        num = float(num) if num else 0
        flist = filter(lambda x: x > num, random_list)
    except Exception as e:
        flist = ["Not a valid Integer!"]
    return render(request, "partials/filter_list.html", {"flist": list(flist)})


# def books_by_date(request):
#     publication_date = request.GET.get('publication_date', datetime.today().date().strftime('%Y-%m-%d'))
#     iprint(type(publication_date), publication_date)
#     books = Book.objects.filter(publication_date=publication_date)
#     if request.headers.get("HX-Request") == "true":
#         return render(request, "partials/books_table.html", {"books": books})
#     return render(request, "books_by_date.html", {"books": books, "publication_date": publication_date})


from django.views.generic import ListView
from django.utils import timezone


class BooksByDateView(ListView):
    model = Book
    context_object_name = "books"

    # Specify default template for full-page loads
    template_name = "books_by_date.html"

    def get_queryset(self):
        # Get the publication_date from GET, or default to today's date
        publication_date = self.request.GET.get(
            "publication_date", timezone.now().date().strftime("%Y-%m-%d")
        )

        return Book.objects.filter(publication_date=publication_date)

    def get_template_names(self):
        # If the request is an HTMX request, render the partial template
        if self.request.headers.get("HX-Request") == "true":
            return ["partials/books_table.html"]
        return [self.template_name]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Include publication_date in context for rendering in template
        context["publication_date"] = self.request.GET.get(
            "publication_date", timezone.now().date().strftime("%Y-%m-%d")
        )
        return context


def books_card_list(request):
    search_query = request.GET.get("search_query", "")
    sort_order = request.GET.get("sort_order", "")
    iprint(request.GET)

    if search_query:
        books = Book.objects.filter(
            Q(title__icontains=search_query)
            | Q(author__icontains=search_query)
            | Q(language__icontains=search_query)
        )
    else:
        books = Book.objects.all()

    if sort_order == "desc":
        books = books.order_by("publication_date")
    elif sort_order == "pasc":
        books = books.order_by("pages")
    elif sort_order == "pdesc":
        books = books.order_by("-pages")
    else:
        books = books.order_by("-publication_date")

    if request.headers.get("HX-Request") == "true":
        return render(request, "partials/books_cards.html", {"books": books})

    return render(request, "books_card_list.html", {"books": books})


from django.http import JsonResponse


def handle_values(request):
    extra_value1 = request.GET.get("extra_value1")
    extra_value2 = request.GET.get("extra_value2")
    iprint(request.GET)
    response_data = {
        "received_value1": extra_value1,
        "received_value2": extra_value2,
        "message": "Values received successfully.",
    }
    if request.headers.get("HX-Request") == "true":
        return JsonResponse(response_data)
    return render(request, "handle_values.html")
