from .base_page import BasePage
from .locators import CartPageLocators

class CartPage(BasePage):
    def should_not_be_product_in_cart(self):
        assert self.is_not_element_present(*CartPageLocators.CART_ITEMS), "Find product in cart, but should not"

    def should_be_text_about_empty_cart(self):
        text_in_cart = self.browser.find_element(*CartPageLocators.EMPTY_CART_TEXT).text
        assert text_in_cart == "Your basket is empty. Continue shopping", "Wrong empty cart text: " + text_in_cart
        