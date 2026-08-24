PRAGMA foreign_keys = OFF;

DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS couriers;

CREATE TABLE couriers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    login TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    first_name TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    track TEXT NOT NULL UNIQUE,
    courier_id INTEGER NOT NULL,
    status TEXT NOT NULL DEFAULT 'NEW',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (courier_id)
        REFERENCES couriers(id)
);