from constants import BASE_URL
from enums import SortProductMenuOptions
from playwright.sync_api import Locator, Page
from pom.components.page_header import PageHeader
from pom.components.product_item import ProductItem


class InventoryPage:
    PAGE_URL = f"{BASE_URL}/inventory.html"

    def __init__(self, *, page: Page):
        self.page = page
        self.page_header = PageHeader(page=page)
        self.active_sort_option = self.page_header.secondary_header.get_by_test_id("active-option")
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


class InventoryItem(ProductItem):
    def __init__(self, *, item: Locator):
        super().__init__(item=item)
        self.add_to_cart_button = item.locator("button[data-test^='add-to-cart-']")
        self.remove_from_cart_button = item.locator("button[data-test^='remove-']")
