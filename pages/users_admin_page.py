from pages.admin_page import AdminPage
from locators.users_admin_page_locators import UsersAdminPageLocators


class UsersAdminPage(AdminPage):

    def add_new_user(self, username, passwd):
        add_user_button = self.find_element(
            UsersAdminPageLocators.ADD_USER_BUTTON_LOCATOR)
        add_user_button.click()

        username_field = self.find_element(
            UsersAdminPageLocators.ADD_USER_USERNAME_FIELD_LOCATOR)
        passwd_field = self.find_element(
            UsersAdminPageLocators.ADD_USER_PASSWORD_FIELD_LOCATOR)
        passwd_confirm_field = self.find_element(
            UsersAdminPageLocators.ADD_USER_PASSWORD_CONFIRM_FIELD_LOCATOR)

        username_field.send_keys(username)
        passwd_field.send_keys(passwd)
        passwd_confirm_field.send_keys(passwd)

        save_button = self.find_element(
            UsersAdminPageLocators.ADD_USER_SAVE_BUTTON_LOCATOR)
        save_button.click()

    def is_add_user_successful(self, username):
        confirm_text = self.find_element(
            UsersAdminPageLocators.ADD_USER_CONFIRM_TEXT_LOCATOR)
        assert confirm_text.text == f'The user “{username}” was added ' \
                                    f'successfully. ' \
                                    f'You may edit it again below.'

    def go_to_some_user_page(self, username):
        user_button = self.find_element(
            UsersAdminPageLocators.GO_TO_USER_PAGE_BUTTON_LOCATOR(username))
        user_button.click()

    def set_staff_status_to_user(self):
        staff_status_checkbox = self.find_element(
            UsersAdminPageLocators.STAFF_STATUS_CHECKBOX_LOCATOR)
        staff_status_checkbox.click()
        save_button = self.find_element(
            UsersAdminPageLocators.SAVE_USER_BUTTON_LOCATOR)
        save_button.click()
