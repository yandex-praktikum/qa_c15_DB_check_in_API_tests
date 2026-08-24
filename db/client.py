from db.connection import create_connection
from db import queries

class DatabaseClient:

    def execute(self, query, params=()):
        with create_connection() as connection:
            cursor = connection.cursor()
            cursor.execute(query, params)
            connection.commit()
            return cursor

    def fetchone(self, query, params=()):
        return self.execute(query, params).fetchone()

    def fetchall(self, query, params=()):
        return self.execute(query, params).fetchall()

    def get_courier_by_id(self, courier_id):
        return self.fetchone(
            queries.GET_COURIER_BY_ID,
            (courier_id,)
        )

    def get_courier_by_login(self, login):
        return self.fetchone(
            queries.GET_COURIER_BY_LOGIN,
            (login,)
        )

    def get_orders_by_courier(self, courier_id):
        return self.fetchall(
            queries.GET_ORDERS_BY_COURIER_ID,
            (courier_id,)
        )

    def create_courier(self, login, password, first_name):
        cursor = self.execute(
            queries.CREATE_COURIER,
            (login, password, first_name)
        )

        return cursor.lastrowid

    def delete_courier(self, courier_id):
        self.execute(
            queries.DELETE_COURIER,
            (courier_id,)
        )

    def delete_orders(self, courier_id):
        self.execute(
            queries.DELETE_ORDERS_BY_COURIER_ID,
            (courier_id,)
        )

    def create_order(self, track, courier_id, status="NEW"):
        self.execute(
            queries.CREATE_ORDER,
            (track, courier_id, status)
        )