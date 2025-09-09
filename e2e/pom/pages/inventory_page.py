from constants import BASE_URL
from enums import SortProductMenuOptions
from playwright.sync_api import Locator, Page


class InventoryPage:
    PAGE_URL = f"{BASE_URL}/inventory.html"

    def __init__(self, *, page: Page):
        self.page = page
        self.primary_header = page.get_by_test_id("primary-header")
        self.open_menu_button = self.primary_header.get_by_test_id("open-menu")
        self.shopping_cart_button = self.primary_header.get_by_test_id("shopping-cart-link")
        self.secondary_header = page.get_by_test_id("secondary-header")
        self.active_sort_option = self.secondary_header.get_by_test_id("active-option")
        self.sort_products_menu = SortProductsMenu(page=page)
        self.inventory_list = page.get_by_test_id("inventory-list")
        self.inventory_items = self.inventory_list.get_by_test_id("inventory-item")
        self.inventory_item_names = self.inventory_items.get_by_test_id("inventory-item-name")

    def get_inventory_item_by_name(self, *, name: str) -> "InventoryItem":
        filtered_item_name = self.inventory_item_names.filter(has_text=name)
        item_locator = self.inventory_items.filter(has=filtered_item_name)

        return InventoryItem(item=item_locator)


class SortProductsMenu:
    def __init__(self, *, page: Page):
        self.page = page
        self.products_sort_menu = page.get_by_test_id("product-sort-container")

    def select_sort_option(self, option: SortProductMenuOptions) -> None:
        self.products_sort_menu.select_option(value=option.value)


class InventoryItem:
    def __init__(self, *, item: Locator):
        self.item = item
        self.item_description = self.item.get_by_test_id("inventory-item-description")
        self.item_name = self.item_description.get_by_test_id("inventory-item-name")
        self.item_price = self.item.get_by_test_id("inventory-item-price")
        self.add_to_cart_button = item.locator("button[data-test^='add-to-cart-']")
        self.remove_from_cart_button = item.locator("button[data-test^='remove-']")
