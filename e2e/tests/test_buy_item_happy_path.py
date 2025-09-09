from e2e.pom.pages.cart_page import CartPage
from e2e.pom.pages.checkout_page import CheckoutPage
from e2e.pom.pages.inventory_page import InventoryPage
from e2e.pom.pages.login_page import LoginPage


def test_buy_one_item_end_to_end(page):
    # Login
    LoginPage(page=page).goto().login(user="standard_user", password="secret_sauce")

    # Inventory
    inventory = InventoryPage(page=page)
    inventory.expect_loaded()
    inventory.add_item_by_id(item_id="sauce-labs-backpack")
    inventory.open_cart()

    # Cart
    cart = CartPage(page=page)
    cart.expect_loaded()
    cart.checkout()

    # Checkout
    checkout = CheckoutPage(page=page)
    checkout.provide_info_and_continue(first_name="Deian", last_name="QA", postal_code="1000")
    checkout.finish()
