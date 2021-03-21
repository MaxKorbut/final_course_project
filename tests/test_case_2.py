from pages.posts_admin_page import PostsAdminPage
import allure


@allure.story("Delete first created post")
def test_delete_first_created_post(browser, get_data_for_admin_login):
    with allure.step("Open app and log in as admin"):
        posts_page = PostsAdminPage(browser)
        first_created_post_src_before_delete = posts_page.get_last_post_src()
        posts_page.open_admin_login_page()
        admin_username, admin_passwd = get_data_for_admin_login
        posts_page.login(admin_username, admin_passwd)

    with allure.step("Delete first created post"):
        posts_page.click_on_button_from_left_admin_page_block("Posts")
        posts_page.delete_first_created_post()

    with allure.step("Open main page and check is post deleted successful"):
        posts_page.click_on_button_from_top_toolbar("View site")
        assert posts_page.is_post_on_page(first_created_post_src_before_delete)
