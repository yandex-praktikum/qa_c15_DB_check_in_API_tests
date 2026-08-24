import uuid

import pytest


@pytest.fixture
def courier(api, db):

    login = f"courier_{uuid.uuid4().hex[:8]}"

    response = api.create_courier(
        login=login,
        password="1234",
        first_name="Test"
    )

    assert response.status_code == 201

    courier = db.get_courier_by_login(login)

    assert courier is not None

    courier_id = courier[0]

    db.create_order(
        track=f"TRACK-{uuid.uuid4().hex[:8]}",
        courier_id=courier_id
    )

    yield courier_id

    db.delete_orders(courier_id)
    db.delete_courier(courier_id)