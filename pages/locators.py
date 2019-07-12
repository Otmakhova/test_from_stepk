from selenium.webdriver.common.by import By


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
    
    