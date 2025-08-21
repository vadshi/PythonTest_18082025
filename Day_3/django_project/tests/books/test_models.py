from django.urls import reverse


def test_book_content(book):
    assert book.title == "Introducing Python 3-rd Edition"
    assert book.author == "Bill Lubanovich"
    assert book.description == "Learn Python fundamentals"


def test_book_slug(book):
    assert book.slug == "introducing-python-3-rd-edition"
    assert book.slug != "introducing-python-2-nd-edition"
    assert book.slug != "introducing-python-1-st-edition"


def test_book_methods(book):
    assert str(book) == "Introducing Python 3-rd Edition"
    assert book.get_absolute_url() ==  reverse("books:book_detail", kwargs={"slug": book.slug})