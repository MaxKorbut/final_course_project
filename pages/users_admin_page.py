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
            UsersAdminPageLocators.GO_TO_USER_PAGE_LOCATOR(username))
        user_button.click()

    def give_staff_status_to_user(self):
        give_status_button = self.find_element(
            UsersAdminPageLocators.STAFF_STATUS_BUTTON_LOCATOR)
        give_status_button.click()
        save_button = self.find_element(
            UsersAdminPageLocators.SAVE_BUTTON_USER_PAGE_LOCATOR)
        save_button.click()
