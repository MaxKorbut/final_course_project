from selenium.webdriver.common.by import By


class BasePageLocators:

    FIRST_POSTED_POST_LOCATOR = (
        By.XPATH, '(//div[@class="card mb-4 box-shadow"])[last()]')
    FIRST_POSTED_POST_SCR_LOCATOR = (
        By.XPATH, '(//div[@class="card mb-4 box-shadow"])[last()]/img')
