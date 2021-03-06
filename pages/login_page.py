from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in str(
            self.browser.current_url), "'login' is not in current url"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_FORM), "Form to login is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(
            *LoginPageLocators.REGISTRATION_FORM), "Form to register is not presented"

    def register_new_user(self, email, password):
        self.browser.find_element(
            *LoginPageLocators.EMAIL_REGISTRATION_INPUT).send_keys(email)
        self.browser.find_element(
            *LoginPageLocators.PASSWORD_REGISTRATION_INPUT).send_keys(password)
        self.browser.find_element(
            *LoginPageLocators.PASSWORD_CONFIRM_REGISTRATION_INPUT).send_keys(password)
        self.browser.find_element(
            *LoginPageLocators.REGISTRATION_BUTTON).click()
