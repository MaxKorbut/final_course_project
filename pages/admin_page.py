from locators.admin_page_locators import AdminPageLocators
from pages.base_page import BasePage


class AdminPage(BasePage):

    def open_admin_login_page(self):
        go_to_admin_button = self.find_element(
            AdminPageLocators.GO_TO_ADMIN_BUTTON_LOCATOR)
        go_to_admin_button.click()

    def fill_login_form(self, username_value, passwd_value):
        username_field = self.find_element(
            AdminPageLocators.USERNAME_FIELD_LOCATOR)
        passwd_field = self.find_element(
            AdminPageLocators.PASSWORD_FIELD_LOCATOR)
        login_button = self.find_element(
            AdminPageLocators.LOG_IN_BUTTON_LOCATOR)

        username_field.send_keys(username_value)
        passwd_field.send_keys(passwd_value)
        login_button.click()

    def should_be_admin_page(self):
        site_admin_text = self.find_element(
            AdminPageLocators.SITE_ADMIN_TEXT_LOCATOR)
        assert site_admin_text.text == "Site administration"

    def do_something_on_top_toolbar(self, need_page):
        view_site_button = self.find_element(
            AdminPageLocators.get_header_toolbar_locator(need_page))
        view_site_button.click()
