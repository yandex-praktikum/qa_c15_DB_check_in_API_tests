from api.responses import Response
from db.client import DatabaseClient


class FakeAPI:

    def __init__(self):
        self.db = DatabaseClient()

    def create_courier(self, login, password, first_name):
        self.db.create_courier(
            login,
            password,
            first_name
        )

        return Response(
            status_code=201,
            body={
                "ok": True
            }
        )

    def delete_courier(self, courier_id):
        courier = self.db.get_courier_by_id(courier_id)

        if courier is None:
            return Response(
                status_code=404,
                body={
                    "message": "Курьер не найден"
                }
            )

        self.db.delete_courier(courier_id)

        # Скрытый дефект стенда:
        # связанные заказы не удаляются.

        return Response(
            status_code=200,
            body={
                "ok": True
            }
        )