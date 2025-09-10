from playwright.sync_api import Locator


class ProductItem:
    def __init__(self, *, item: Locator):
        self.item = item
        self.item_description = self.item.get_by_test_id("inventory-item-description")
        self.item_name = self.item_description.get_by_test_id("inventory-item-name")
        self.item_price = self.item.get_by_test_id("inventory-item-price")
        self.add_to_cart_button = item.locator("button[data-test^='add-to-cart-']")
        self.remove_from_cart_button = item.locator("button[data-test^='remove-']")
