from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product_to_basket(self):
        price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()
        self.solve_quiz_and_get_code()
        self.should_be_same_book_name_in_alert(name)
        self.should_be_same_price_in_alert(price)

    def should_be_same_book_name_in_alert(self, name):
        success_alert_text = self.browser.find_element(*ProductPageLocators.SUCCESS_ALERT_TEXT).text
        assert success_alert_text == name + " has been added to your basket.",  "Неверный текст успешного добавления в корзину: " +  success_alert_text

    def should_be_same_price_in_alert(self, price):
        full_price_alert_text = self.browser.find_element(*ProductPageLocators.PRICE_ALERT_TEXT).text
        assert full_price_alert_text == "Your basket total is now " + price, "Неверные текст стоимости корзины: " + full_price_alert_text

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_ALERT_TEXT), "Success message is presented, but should not be"

    def should_disappear_after_add(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_ALERT_TEXT), "Success message do not dissapeared after 4 sec, but should"


    

        