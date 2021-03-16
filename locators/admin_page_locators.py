from selenium.webdriver.common.by import By


class AdminPageLocators:

    ADMIN_BUTTON_LOCATOR = (By.XPATH,
                                  '//a[@class="btn btn-primary my-2"]')
    USERNAME_FIELD_LOCATOR = (By.XPATH, '//div[@id="content-main"]'
                                        '//input[@name="username"]')
    PASSWORD_FIELD_LOCATOR = (By.XPATH, '//div[@id="content-main"]'
                                        '//input[@name="password"]')
    LOG_IN_BUTTON_LOCATOR = (By.XPATH, '//div[@id="content-main"]'
                                       '//input[@type="submit"]')
    SITE_ADMIN_TEXT_LOCATOR = (By.XPATH, '//div[@id="content"]//h1')

    @staticmethod
    def TOP_TOOLBAR_BUTTON_LOCATOR(toolbar_button: str):
        toolbar_element_locator = (
            By.XPATH, f'//div[@id="header"]'
                      f'//a[text()="{toolbar_button.capitalize()}"]')
        return toolbar_element_locator

    USERNAME_IN_HEADER_LOCATOR = (By.XPATH, '//div[@id="user-tools"]//strong')

    @staticmethod
    def LOCATOR_BUTTON_FROM_LEFT_BLOCK(button_name):
        button_locator = (By.XPATH, f'//div[@id="content-main"]'
                                    f'//a[text()="{button_name}"]')
        return button_locator
