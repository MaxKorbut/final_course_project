from pages.admin_page import AdminPage
from pages.users_admin_page import UsersAdminPage
from database.db import DataBase


def test_case_1(browser, get_data_for_admin_login, get_data_for_add_user):
    admin_page = AdminPage(browser)
    admin_page.open_admin_login_page()
    admin_username, admin_passwd = get_data_for_admin_login
    admin_page.fill_login_form(admin_username, admin_passwd)

    admin_user_page = UsersAdminPage(browser)
    admin_user_page.go_to_page_from_auth_app_block("Users")
    new_username, new_passwd = get_data_for_add_user
    admin_user_page.add_new_user(new_username, new_passwd)
    admin_user_page.give_staff_status_to_user()

    db = DataBase()
    db.is_user_in_auth_table(new_username)

    admin_page.go_to_something_page_from_top_toolbar("Log out")
    admin_page.go_to_something_page_from_top_toolbar("Django administration")
    admin_page.fill_login_form(new_username, new_passwd)
    admin_page.is_login_successful(new_username)
