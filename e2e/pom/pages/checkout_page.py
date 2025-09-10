from playwright.sync_api import Page
from pom.components.page_header import PageHeader
from pom.components.product_item import ProductItem


class CheckoutPage:
    def __init__(self, *, page: Page):
        self.page = page
        self.page_header = PageHeader(page=page)

        # Step 1: Info form
        self.first_name = page.get_by_test_id("firstName")
        self.last_name = page.get_by_test_id("lastName")
        self.postal_code = page.get_by_test_id("postalCode")
        self.cancel_button = page.get_by_test_id("cancel")
        self.continue_button = page.get_by_test_id("continue")

        # Step 2: Overview
        self.finish_button = page.get_by_test_id("finish")
        self.summary_subtotal = page.get_by_test_id("subtotal-label")
        self.summary_tax = page.get_by_test_id("tax-label")
        self.summary_total = page.get_by_test_id("total-label")

        # Step 3: Complete checkout
        self.complete_header = page.get_by_text("Thank you for your order!", exact=True)
        self.back_home_button = page.get_by_test_id("back-to-products")

        # Items list
        self.items_list = page.get_by_test_id("cart_list")
        self.items = self.items_list.get_by_test_id("inventory-item")
        self.item_names = self.items.get_by_test_id("inventory-item-name")

    def get_item_by_name(self, *, name: str) -> ProductItem:
        filtered_item_name = self.item_names.filter(has_text=name)
        item_locator = self.items.filter(has=filtered_item_name)

        return ProductItem(item=item_locator)

    def provide_info_and_continue(self, *, first_name: str, last_name: str, postal_code: str):
        self.first_name.fill(first_name)
        self.last_name.fill(last_name)
        self.postal_code.fill(postal_code)
        self.continue_button.click()
