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
            message=f"Can not find elements {locator}"
        )

    def is_post_on_page(self, post_src: str, time=10):
        locator = BasePageLocators.GET_POST_SRC_LOCATOR(post_src)
        return WebDriverWait(self.driver, time).until_not(
            EC.visibility_of_element_located(locator),
            message=f"Can not find element {locator}"
        )

    def get_last_post_src(self):
        unique_src = self.find_element(
            BasePageLocators.FIRST_POSTED_POST_SCR_LOCATOR).get_attribute("src")
        return unique_src
