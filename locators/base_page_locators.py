from selenium.webdriver.common.by import By


class BasePageLocators:

    FIRST_POSTED_POST_LOCATOR = (
        By.XPATH, '(//div[@class="card mb-4 box-shadow"])[last()]')
    FIRST_POSTED_POST_SCR_LOCATOR = (
        By.XPATH, '(//div[@class="card mb-4 box-shadow"])[last()]/img')

    @staticmethod
    def GET_POST_SRC_LOCATOR(post_src: str):
        post_src_locator = (By.XPATH, f'//div[@class="card mb-4 box-shadow"]'
                                      f'//img[@src="{post_src}"]')
        return post_src_locator
