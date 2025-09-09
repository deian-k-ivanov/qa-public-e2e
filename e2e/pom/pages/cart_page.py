from constants import BASE_URL
from playwright.sync_api import Locator, Page


class ShoppingCartPage:
    PAGE_URL = f"{BASE_URL}/cart.html"

    def __init__(self, *, page: Page):
        self.page = page

        # Headers / Title
        self.primary_header = page.get_by_test_id("primary-header")
        self.shopping_cart_button = self.primary_header.get_by_test_id("shopping-cart-link")
        self.shopping_cart_badge = self.shopping_cart_button.get_by_test_id("shopping-cart-badge")
        self.page_title = page.get_by_test_id("title")

        # Cart content
        self.cart_list = page.get_by_test_id("cart-list")
        self.cart_items = self.cart_list.get_by_test_id("inventory-item")
        self.cart_item_names = self.cart_items.get_by_test_id("inventory-item-name")

        # Actions
        self.continue_shopping_button = page.get_by_test_id("continue-shopping")
        self.checkout_button = page.get_by_test_id("checkout")

    def goto(self) -> "ShoppingCartPage":
        self.page.goto(self.PAGE_URL)
        return self

    def get_cart_item_by_name(self, *, name: str) -> "CartItem":
        filtered_name = self.cart_item_names.filter(has_text=name)
        item_locator = self.cart_items.filter(has=filtered_name)

        return CartItem(item=item_locator)


class CartItem:
    def __init__(self, *, item: Locator):
        self.item = item
        self.item_description = self.item.get_by_test_id("inventory-item-description")
        self.item_name = self.item_description.get_by_test_id("inventory-item-name")
        self.item_price = self.item.get_by_test_id("inventory-item-price")
        self.quantity = self.item.get_by_test_id("cart-quantity")
        self.remove_button = self.item.locator("button[data-test^='remove-']")
