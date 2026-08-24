-- Проверка связанных заказов после удаления курьера

SELECT
    id,
    track,
    status,
    courier_id
FROM orders
WHERE courier_id = :courier_id;