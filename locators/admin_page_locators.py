from selenium.webdriver.common.by import By


class AdminPageLocators:

    GO_TO_ADMIN_BUTTON_LOCATOR = (By.XPATH,
                                  '//a[@class="btn btn-primary my-2"]')
    USERNAME_FIELD_LOCATOR = (By.XPATH, '//input[@name="username"]')
    PASSWORD_FIELD_LOCATOR = (By.XPATH, '//input[@name="password"]')
    LOG_IN_BUTTON_LOCATOR = (By.XPATH, '//input[@value="Log in"]')
    SITE_ADMIN_TEXT_LOCATOR = (By.XPATH, '//div[@class="colMS"]//h1')

    @staticmethod
    def get_header_toolbar_locator(toolbar_element: str):
        toolbar_element_locator = (
            By.XPATH, f'//div[@id="header"]'
                      f'//a[text()="{toolbar_element.capitalize()}"]')
        return toolbar_element_locator
