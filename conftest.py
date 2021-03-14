import pytest
from selenium import webdriver
import os.path
import json


@pytest.fixture()
def browser():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get("http://localhost:8000/")
    yield driver
    driver.quit()


def load_config(file_path):
    config_path = \
        os.path.join(os.path.dirname(os.path.abspath(__file__)), file_path)
    with open(config_path) as f:
        data = json.load(f)
    return data


@pytest.fixture()
def get_data_for_admin_login():
    admin_data = load_config("resources/variables/admin_login_data.json")
    username_value = admin_data["ID"]
    passwd_value = admin_data["PW"]
    return username_value, passwd_value


@pytest.fixture()
def get_data_for_add_user():
    user_data = load_config("resources/variables/add_user_data.json")
    new_user_name = user_data["username"]
    new_user_passwd = user_data["passwd"]
    return new_user_name, new_user_passwd


@pytest.fixture()
def get_data_to_add_pet():
    new_pet_json = load_config("resources/variables/data_to_add_new_pet.json")
    return new_pet_json


@pytest.fixture()
def get_data_to_update_pet():
    update_pet_json = load_config(
        "resources/variables/data_to_update_pet.json")
    return update_pet_json
