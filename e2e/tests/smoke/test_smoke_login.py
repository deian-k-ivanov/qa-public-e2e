import pytest
from constants import PASSWORD, STANDARD_USER
from playwright.sync_api import expect

from e2e.pom.pages.login_page import LoginPage


@pytest.mark.smoke
def test_login_smoke(page):
    # Setup
    login_page = LoginPage(page=page)

    # Steps
    login_page.goto()
    inventory_page = login_page.login(user=STANDARD_USER, password=PASSWORD)

    # Assertions
    expect(inventory_page.shopping_cart_button).to_be_visible()
