from locators.admin_page_locators import AdminPageLocators
from pages.base_page import BasePage


class AdminPage(BasePage):

    def open_admin_login_page(self):
        go_to_admin_button = self.find_element(
            AdminPageLocators.ADMIN_BUTTON_LOCATOR)
        go_to_admin_button.click()

    def login(self, username: str, passwd: str):
        username_field = self.find_element(
            AdminPageLocators.USERNAME_FIELD_LOCATOR)
        passwd_field = self.find_element(
            AdminPageLocators.PASSWORD_FIELD_LOCATOR)
        login_button = self.find_element(
            AdminPageLocators.LOG_IN_BUTTON_LOCATOR)

        username_field.send_keys(username)
        passwd_field.send_keys(passwd)
        login_button.click()

    def should_be_admin_page(self):
        site_admin_text = self.find_element(
            AdminPageLocators.SITE_ADMIN_TEXT_LOCATOR)
        assert site_admin_text.text == "Site administration"

    def click_on_button_from_top_toolbar(self, need_button):
        view_site_button = self.find_element(
            AdminPageLocators.TOP_TOOLBAR_BUTTON_LOCATOR(need_button))
        view_site_button.click()

    def is_login_successful(self, username: str):
        username_text = self.find_element(
            AdminPageLocators.USERNAME_IN_HEADER_LOCATOR)
        assert username_text.text.upper() == username.upper()

    def click_on_button_from_left_admin_page_block(self, button_name: str):
        users_button = self.find_element(
            AdminPageLocators.LOCATOR_BUTTON_FROM_LEFT_BLOCK(button_name))
        users_button.click()
