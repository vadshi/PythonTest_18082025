from django.urls import reverse, resolve
import pytest
from pytest_django.asserts import assertContains, assertNotContains, assertTemplateUsed

from books.views import BookListView, BookDetailView


@pytest.mark.django_db
def test_book_list_view(book_list_response):
    url = reverse("books:book_list")
    view = resolve(url)

    assert book_list_response.status_code == 200 # OK
    assert view.func.view_class == BookListView # type: ignore

    assertContains(book_list_response, "Books")
    assertNotContains(book_list_response, "Hi! Absent info")
    assertTemplateUsed(book_list_response, "books/list.html")


@pytest.mark.django_db
def test_book_list_view_context(book, book_list_response):
    assert "books" in book_list_response.context
    assert len(book_list_response.context["books"]) == 1



@pytest.mark.django_db
def test_book_detail_view(book, book_detail_response):
    url = reverse("books:book_detail", kwargs={"slug": book.slug})
    view = resolve(url)

    assert book_detail_response.status_code == 200 # OK
    assert view.func.view_class == BookDetailView # type: ignore

    assertContains(book_detail_response, book.title)
    assertNotContains(book_detail_response, "Hi! Absent info")
    assertTemplateUsed(book_detail_response, "books/detail.html")


@pytest.mark.django_db
def test_book_detail_view_context(book, book_detail_response):
    assert "book" in book_detail_response.context
    assert book_detail_response.context["book"] == book