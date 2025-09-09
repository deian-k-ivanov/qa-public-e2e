from constants import BASE_URL
from playwright.sync_api import Page
from pom.pages.inventory_page import InventoryPage


class LoginPage:
    def __init__(self, *, page: Page):
        self.page = page
        self.username_input = page.get_by_test_id("username")
        self.password_input = page.get_by_test_id("password")
        self.login_button = page.get_by_test_id("login-button")
        self.error_banner = page.get_by_test_id("error")

    def goto(self):
        self.page.goto(BASE_URL)
        return self

    def login(self, *, user: str, password: str) -> InventoryPage:
        self.username_input.fill(user)
        self.password_input.fill(password)
        self.login_button.click()

        return InventoryPage(page=self.page)
