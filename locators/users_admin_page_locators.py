from selenium.webdriver.common.by import By


class UsersAdminPageLocators:

    USERS_BUTTON_LOCATOR = (By.XPATH, '//a[text()="Users"]')
    ADD_USER_BUTTON_LOCATOR = (By.XPATH, '//ul[@class="object-tools"]//a')
    ADD_USER_USERNAME_FIELD_LOCATOR = (
        By.XPATH, '//input[@class="vTextField"]')
    ADD_USER_PASSWORD_FIELD_LOCATOR = (By.XPATH, '//input[@name="password1"]')
    ADD_USER_PASSWORD_CONFIRM_FIELD_LOCATOR = (
        By.XPATH, '//input[@name="password2"]')
    ADD_USER_SAVE_BUTTON_LOCATOR = (By.XPATH, '//input[@class="default"]')
    ADD_USER_CONFIRM_TEXT_LOCATOR = (By.XPATH, '//li[@class="success"]')
