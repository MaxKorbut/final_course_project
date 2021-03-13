from pages.admin_page import AdminPage
from locators.users_admin_page_locators import UsersAdminPageLocators


class UsersAdminPage(AdminPage):

    def go_to_users_page(self):
        users_button = self.find_element(
            UsersAdminPageLocators.USERS_BUTTON_LOCATOR)
        users_button.click()

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
