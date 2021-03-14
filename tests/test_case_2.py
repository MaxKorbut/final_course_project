from pages.posts_admin_page import PostsAdminPage


def test_case_2(browser, get_data_for_admin_login):
    posts_page = PostsAdminPage(browser)
    last_post_src_before_delete = posts_page.get_last_post_src()

    posts_page.open_admin_login_page()
    admin_username, admin_passwd = get_data_for_admin_login
    posts_page.fill_login_form(admin_username, admin_passwd)
    posts_page.go_to_posts_page()
    posts_page.delete_first_posted_post()
    posts_page.do_something_on_top_toolbar("View site")

    last_post_src_after_delete = posts_page.get_last_post_src()
    assert last_post_src_before_delete != last_post_src_after_delete
