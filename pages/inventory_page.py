class InventoryPage:
    def __init__(self, page):
        self.page = page
        self.cart_badge = ".shopping_cart_badge"
        self.first_add_to_cart_button = ".inventory_item button"

    def add_first_item_to_cart(self):
        self.page.click(self.first_add_to_cart_button)

    def get_cart_count(self):
        return self.page.text_content(self.cart_badge)
