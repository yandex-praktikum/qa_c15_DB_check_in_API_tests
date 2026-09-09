from api.fake_api import FakeAPI


class ApiClient:

    def __init__(self):
        self.api = FakeAPI()

    def create_courier(self, login, password, first_name):
        return self.api.create_courier(
            login,
            password,
            first_name
        )

    def delete_courier(self, courier_id):
        return self.api.delete_courier(courier_id)