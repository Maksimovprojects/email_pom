from selenium.webdriver.common.by import By


class LoginPageLocators:
    USER = (By.CSS_SELECTOR, "[name = 'login']")
    MAIL_DOMAIN = (By.CSS_SELECTOR, "option:nth-child(3)")
    PASSWORD = (By.CSS_SELECTOR, "[data-testid = 'password-input']")
    LOGIN_FORM = (By.CSS_SELECTOR, "[type='password']")
    REGISTER_BUTTON = (By.XPATH, "//a[contains(text(),'Регистрация')]")
    ENTER_PASSWORD_BUTTON = (By.CSS_SELECTOR, "[data-testid = 'enter-password']")
    ENTER_BUTTON = (By.CSS_SELECTOR, "[data-testid ='login-to-mail']")


class MainPageLocators:
    WRITE_EMAIL = (By.CSS_SELECTOR, "[class='compose-button__wrapper']")


class TestData:
    CHROME_DRIVER_PATH = "write your own pathway to driver"
    FIREFOX_GECKODRIVER_PATH = "write your own pathway to driver"
    LOGIN_URL = "https://mail.ru/"
    USERNAME = "your_username"
    PASSWORD = "your_password"


