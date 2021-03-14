from pages.posts_admin_page import PostsAdminPage


def test_case_2(browser, get_data_for_admin_login):
    posts_page = PostsAdminPage(browser)
    last_post_src_before_delete = posts_page.get_last_post_src()

    posts_page.open_admin_login_page()
    admin_username, admin_passwd = get_data_for_admin_login
    posts_page.fill_login_form(admin_username, admin_passwd)

    posts_page.go_to_page_from_auth_app_block("Posts")
    posts_page.delete_first_posted_post()
    posts_page.go_to_something_page_from_top_toolbar("View site")

    last_post_src_after_delete = posts_page.get_last_post_src()
    assert last_post_src_before_delete != last_post_src_after_delete
    assert posts_page.is_post_on_page(last_post_src_before_delete)
