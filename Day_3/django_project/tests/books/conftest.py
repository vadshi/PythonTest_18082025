import pytest
from django.urls import reverse

from books.models import Book


@pytest.fixture
def book(db):
    return Book.objects.create(
        title="Introducing Python 3-rd Edition",
        author="Bill Lubanovich",
        description="Learn Python fundamentals",
        slug="introducing-python-3-rd-edition"
    )


@pytest.fixture
def book_list_response(client):
    url = reverse("books:book_list")
    return client.get(url)


@pytest.fixture
def book_detail_response(book, client):
    url = reverse("books:book_detail", kwargs={"slug": book.slug})
    return client.get(url)