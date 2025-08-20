from django.urls import reverse, resolve
from pytest_django.asserts import assertContains, assertNotContains, assertTemplateUsed

from pages.views import HomePageView


def test_homepage_view(home_response):
    url = reverse("pages:home")
    view = resolve(url)

    assert home_response.status_code == 200 # OK
    assert view.func.view_class == HomePageView # type: ignore

    assertContains(home_response, "Hello students!")
    assertNotContains(home_response, "Hi! Absent info")
    assertTemplateUsed(home_response, "pages/home.html")
