import time
import pytest
from selenium import webdriver

from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.locators import LoginPageLocators
from pages.locators import MainPageLocators
from pages.locators import TestData

@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


def test_quest_can_go_to_login_page(browser):
    link = "https://mail.ru/"
    login_page = LoginPage(browser, link)  # initial Page Object, send to constructor instance of driver and url
    login_page.open()
    login_page.should_be_login_page()
    user_name = browser.find_element(*LoginPageLocators.USER)
    user_name.send_keys(*TestData.USERNAME)
    choose_mail_domain = browser.find_element(*LoginPageLocators.MAIL_DOMAIN)
    choose_mail_domain.click()
    browser.find_element(*LoginPageLocators.ENTER_PASSWORD_BUTTON).click()
    enter_password = browser.find_element(*LoginPageLocators.PASSWORD)
    enter_password.send_keys(*TestData.PASSWORD)
    enter_button = browser.find_element(*LoginPageLocators.ENTER_BUTTON)
    enter_button.click()

    # ОСТАЛОСЬ ПАРУ ШАГОВ ДОДЕЛАТЬ!!!!
    # write_email = browser.find_element(*MainPageLocators.WRITE_EMAIL)
    # write_email.click()

