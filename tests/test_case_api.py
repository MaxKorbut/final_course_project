from pages.api.pet_api_page import PetApiPage
import allure


@allure.story("Add new pet and update his name")
def test_add_pet_update_his_name(get_data_to_add_pet, get_data_to_update_pet):
    with allure.step("Add new pet"):
        new_pet_json = get_data_to_add_pet
        pet_page = PetApiPage()
        pet_page.add_new_pet_to_market(new_pet_json)

    with allure.step("Check is new pet added successful"):
        pet_id = new_pet_json["id"]
        pet_page.check_if_pet_in_market(pet_id)

    with allure.step("Update pet name"):
        update_pet_json = get_data_to_update_pet
        pet_name_before_update = pet_page.get_pet_name(pet_id)
        pet_page.update_pet_data(update_pet_json)

    with allure.step("Check is update successful"):
        pet_name_after_update = pet_page.get_pet_name(pet_id)
        assert pet_name_before_update != pet_name_after_update
