import requests
import json


class PetApiPage:

    def __init__(self):
        self.url = "https://petstore.swagger.io/v2/pet"

    def add_new_pet_to_market(self, new_pet_json_data):
        response = requests.post(self.url, json=new_pet_json_data)
        assert response.status_code == 200

    def check_if_pet_in_market(self, pet_id):
        response = requests.get(self.url+"/"+str(pet_id))
        assert response.status_code == 200

    def update_pet_data(self, pet_json_data_new):
        response = requests.put(self.url, json=pet_json_data_new)
        assert response.status_code == 200

    def get_pet_name(self, pet_id):
        pet_data = requests.get(self.url+"/"+str(pet_id)).text
        pet_data = json.loads(pet_data)
        return pet_data["name"]
