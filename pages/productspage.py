from playwright.sync_api import expect

from pages.basepage import BasePage


class ProductPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self._TITLE = page.locator("[data-test='title']")
        self._ADD_TO_CART_BTN = "[data-test='add-to-cart-{0}']"
        self._REMOVE_FROM_CART_BTN = "[data-test='remove-{0}']"
        self._CART_BADGE_NUM = "[data-test='shopping-cart-badge']"

    def add_to_cart(self, product_name):
        if isinstance(product_name, str):
            element = self._ADD_TO_CART_BTN.format(product_name.replace(" ", "-").lower())
            self.click(element)
        elif isinstance(product_name, list):
            for product in product_name:
                element = self._ADD_TO_CART_BTN.format(product.replace(" ", "-").lower())
                self.click(element)

    def remove_from_cart(self, product_name):
        if isinstance(product_name, str):
            element= self._REMOVE_FROM_CART_BTN.format(product_name.replace(" ", "-").lower())
            self.click(element)

    def get_remove_button(self, product_name):
        slug = product_name.replace(" ", "-").lower()
        return self.page.locator(self._REMOVE_FROM_CART_BTN.format(slug))

    def get_cart_count(self):
        return int(self.page.locator(self._CART_BADGE_NUM).inner_text())
