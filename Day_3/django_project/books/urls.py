from django.urls import path
from .views import BookDetailView, BookListView

app_name = "books"
urlpatterns = [
    path("", BookListView.as_view(), name="book_list"),
    path("<slug:slug>/", BookDetailView.as_view(), name="book_detail"),
]