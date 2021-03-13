from pages.admin_page import AdminPage
from locators.posts_admin_page_locators import PostsAdminPageLocators
from selenium.webdriver.support.ui import Select


class PostsAdminPage(AdminPage):

    def go_to_posts_page(self):
        posts_button = self.find_element(
            PostsAdminPageLocators.POSTS_BUTTON_LOCATOR)
        posts_button.click()

    def delete_first_posted_post(self):
        select_last_post_button = self.find_element(
            PostsAdminPageLocators.FIRST_POSTED_POST_SELECT_LOCATOR)
        select_last_post_button.click()

        select_action_element = Select(self.find_element(
            PostsAdminPageLocators.SELECT_ACTION_LOCATOR))
        select_action_element.select_by_visible_text("Delete selected posts")

        go_button = self.find_element(
            PostsAdminPageLocators.GO_BUTTON_LOCATOR)
        go_button.click()

        yes_button = self.find_element(
            PostsAdminPageLocators.YES_BUTTON_LOCATOR)
        yes_button.click()
