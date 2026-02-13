from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_valid_login(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    assert "inventory" in page.url


def test_add_item_to_cart(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    inventory_page.add_first_item_to_cart()

    cart_count = inventory_page.get_cart_count()
    assert cart_count == "5"


def test_invalid_login(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("wrong_user", "wrong_pass")

    assert "inventory" not in page.url
