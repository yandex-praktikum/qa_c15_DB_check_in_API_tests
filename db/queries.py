GET_COURIER_BY_ID = """
SELECT
    id,
    login,
    first_name
FROM couriers
WHERE id = ?;
"""

GET_ORDERS_BY_COURIER_ID = """
SELECT
    id,
    track,
    status
FROM orders
WHERE courier_id = ?;
"""

CREATE_COURIER = """
INSERT INTO couriers (
    login,
    password,
    first_name
)
VALUES (?, ?, ?);
"""

DELETE_COURIER = """
DELETE FROM couriers
WHERE id = ?;
"""

DELETE_ORDERS_BY_COURIER_ID = """
DELETE FROM orders
WHERE courier_id = ?;
"""

GET_COURIER_BY_LOGIN = """
SELECT
    id,
    login,
    first_name
FROM couriers
WHERE login = ?;
"""

CREATE_ORDER = """
INSERT INTO orders (
    track,
    courier_id,
    status
)
VALUES (?, ?, ?);
"""