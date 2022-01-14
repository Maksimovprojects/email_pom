
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def do_click(self, by_locator):
        element = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(by_locator))
        element.click()

    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def is_element_present(self, how, locator):
        try:
            self.browser.find_element(how, locator)
        except NoSuchElementException:
            return False
        return True

