from pathlib import Path
import sqlite3

ROOT = Path(__file__).parent

DATABASE = ROOT / "samokat.db"
SCHEMA = ROOT / "schema.sql"


def create_database():

    if DATABASE.exists():
        DATABASE.unlink()

    connection = sqlite3.connect(DATABASE)

    with open(SCHEMA, encoding="utf-8") as file:
        connection.executescript(file.read())

    cursor = connection.cursor()

    couriers = [
        ("ivan", "1234", "Ivan"),
        ("petr", "1234", "Petr"),
        ("alex", "1234", "Alex"),
    ]

    cursor.executemany(
        """
        INSERT INTO couriers(login, password, first_name)
        VALUES (?, ?, ?)
        """,
        couriers,
    )

    orders = [
        ("TRACK-1001", 1, "NEW"),
        ("TRACK-1002", 1, "NEW"),
        ("TRACK-1003", 2, "DELIVERED"),
        ("TRACK-1004", 3, "NEW"),
    ]

    cursor.executemany(
        """
        INSERT INTO orders(track, courier_id, status)
        VALUES (?, ?, ?)
        """,
        orders,
    )

    connection.commit()
    connection.close()

    print("Database created")


if __name__ == "__main__":
    create_database()