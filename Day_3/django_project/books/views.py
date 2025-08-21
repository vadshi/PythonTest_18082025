from django.views.generic import DetailView, ListView
from .models import Book

# Create your views here.


class BookListView(ListView):
    model = Book
    context_object_name = "books"
    template_name = "books/list.html"


class BookDetailView(DetailView):
    model = Book
    context_object_name = "book"
    template_name = "books/detail.html"