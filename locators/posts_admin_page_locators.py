from selenium.webdriver.common.by import By


class PostsAdminPageLocators:

    FIRST_CREATED_POST_CHECKBOX_LOCATOR = (
        By.XPATH, '(//div[@class="results"]//tbody//tr)[last()]//input')
    SELECT_ACTION_LOCATOR = (By.XPATH, '//select[@name="action"]')
    GO_BUTTON_LOCATOR = (By.XPATH, '//button[@class="button"]')
    YES_BUTTON_LOCATOR = (By.XPATH, '//input[@type="submit"]')
