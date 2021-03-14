from pages.pet_api_page import PetApiPage


def test_case_api(get_data_to_add_pet, get_data_to_update_pet):
    new_pet_json = get_data_to_add_pet
    update_pet_json = get_data_to_update_pet
    pet_page = PetApiPage()
    pet_page.add_new_pet_to_market(new_pet_json)

    pet_id = new_pet_json["id"]
    pet_page.check_if_pet_in_market(pet_id)

    pet_name_before_update = pet_page.get_pet_name(pet_id)
    pet_page.update_pet_data(update_pet_json)

    pet_name_after_update = pet_page.get_pet_name(pet_id)
    assert pet_name_before_update != pet_name_after_update
