from playwright.sync_api import Page


class PageHeader:
    def __init__(self, *, page: Page):
        self.page = page
        self.primary_header = page.get_by_test_id("primary-header")
        self.open_menu_button = self.primary_header.get_by_test_id("open-menu")
        self.shopping_cart_button = self.primary_header.get_by_test_id("shopping-cart-link")
        self.shopping_cart_badge = self.shopping_cart_button.get_by_test_id("shopping-cart-badge")
        self.secondary_header = page.get_by_test_id("secondary-header")
