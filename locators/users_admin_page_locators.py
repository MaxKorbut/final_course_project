from selenium.webdriver.common.by import By


class UsersAdminPageLocators:

    ADD_USER_BUTTON_LOCATOR = (By.XPATH, '//div[@id="content"]'
                                         '//ul[@class="object-tools"]//a')
    ADD_USER_USERNAME_FIELD_LOCATOR = (
        By.XPATH, '//input[@class="vTextField"]')
    ADD_USER_PASSWORD_FIELD_LOCATOR = (By.XPATH, '//input[@name="password1"]')
    ADD_USER_PASSWORD_CONFIRM_FIELD_LOCATOR = (
        By.XPATH, '//input[@name="password2"]')
    ADD_USER_SAVE_BUTTON_LOCATOR = (By.XPATH, '//input[@class="default"]')
    ADD_USER_CONFIRM_TEXT_LOCATOR = (By.XPATH, '//li[@class="success"]')

    @staticmethod
    def GO_TO_USER_PAGE_LOCATOR(username: str):
        go_username_locator = (By.XPATH, f'//form[@id="changelist-form"]'
                                         f'//tr//a[text()="{username}"]')
        return go_username_locator

    STAFF_STATUS_BUTTON_LOCATOR = (By.XPATH, '//div[@class="form-row '
                                             'field-is_staff"]//input')
    SAVE_BUTTON_USER_PAGE_LOCATOR = (By.XPATH, '//div[@class="submit-row"]'
                                               '//input[@value="Save"]')
