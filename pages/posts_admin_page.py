from pages.admin_page import AdminPage
from locators.posts_admin_page_locators import PostsAdminPageLocators
from selenium.webdriver.support.ui import Select


class PostsAdminPage(AdminPage):

    def delete_first_created_post(self):
        select_first_created_post_checkbox = self.find_element(
            PostsAdminPageLocators.FIRST_CREATED_POST_CHECKBOX_LOCATOR)
        select_first_created_post_checkbox.click()

        select_action_element = Select(self.find_element(
            PostsAdminPageLocators.SELECT_ACTION_LOCATOR))
        select_action_element.select_by_visible_text("Delete selected posts")

        go_button = self.find_element(
            PostsAdminPageLocators.GO_BUTTON_LOCATOR)
        go_button.click()

        yes_button = self.find_element(
            PostsAdminPageLocators.YES_BUTTON_LOCATOR)
        yes_button.click()
