from .base_page import BasePage
from .locators import LoginPageLocators
from selenium import webdriver


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in str(self.browser.current_url), "'login' is not in current url" 

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present (*LoginPageLocators.LOGIN_FORM), "Form to login is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present (*LoginPageLocators.REGISTRATION_FORM), "Form to register is not presented"
