from pages.admin_page import AdminPage
from pages.users_admin_page import UsersAdminPage
from database.db import DataBase
import allure


@allure.story("Create new user and log in as new added user")
def test_case_1(browser, get_data_for_admin_login, get_data_for_add_user, db_connect):
    with allure.step("Open app and log in as admin"):
        admin_page = AdminPage(browser)
        admin_page.open_admin_login_page()
        admin_username, admin_passwd = get_data_for_admin_login
        admin_page.login(admin_username, admin_passwd)

    with allure.step("Create user"):
        admin_user_page = UsersAdminPage(browser)
        admin_user_page.click_on_button_from_left_admin_page_block("Users")
        new_username, new_passwd = get_data_for_add_user
        admin_user_page.add_new_user(new_username, new_passwd)
        admin_user_page.set_staff_status_to_user()

    with allure.step("Check is user in db"):
        connect = db_connect
        db = DataBase(connect)
        db.is_user_in_auth_table(new_username)

    with allure.step("Log in as new user"):
        admin_page.click_on_button_from_top_toolbar("Log out")
        admin_page.click_on_button_from_top_toolbar("Django administration")
        admin_page.login(new_username, new_passwd)
        admin_page.is_login_successful(new_username)
