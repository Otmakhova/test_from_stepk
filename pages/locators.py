from selenium.webdriver.common.by import By

class BasePageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    CART_BUTTON = (By.CSS_SELECTOR, ".btn-group")
    CART_BUTTON_INVALID = (By.CSS_SELECTOR, ".btn-group-inc")

class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")

class LoginPageLocators(object):
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    EMAIL_LOGIN_INPUT = (By.CSS_SELECTOR, "#id_login-username")
    PASSWORD_LOGIN_INPUT = (By.CSS_SELECTOR,"#id_login-password")
    ENTER_BUTTON = (By.CSS_SELECTOR,"[name = 'login_submit']")


    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form") 
    EMAIL_REGISTRATION_INPUT = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_REGISTRATION_INPUT = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR,"[name = 'registration_submit']")

class ProductPageLocators(object):
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    SUCCESS_ALERT_TEXT = (By.CSS_SELECTOR, ".alert-success div")
    PRICE_ALERT_TEXT = (By.XPATH, "//div[@class='alert alert-safe alert-noicon alert-info  fade in']/div/p[1]")
    BOOK_NAME = (By.XPATH, "//div/h1")
    BOOK_PRICE = (By.XPATH, "//p[@class = 'price_color']")

class CartPageLocators(object):
    EMPTY_CART_TEXT = (By.CSS_SELECTOR, "#content_inner")
    CART_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    