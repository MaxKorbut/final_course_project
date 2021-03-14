from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.base_page_locators import BasePageLocators


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator: tuple, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator),
            message=f"Can not find element {locator}"
        )

    def find_elements(self, locator: tuple, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_all_elements_located(locator),
            message=f"can not find elements {locator}"
        )

    def get_last_post_src(self):
        unique_src = self.find_element(
            BasePageLocators.FIRST_POSTED_POST_SCR_LOCATOR).get_attribute("src")
        return unique_src
