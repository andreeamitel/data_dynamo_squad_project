DROP DATABASE IF EXISTS test_sales_orders;

CREATE DATABASE test_sales_orders;

\c test_sales_orders

CREATE TABLE currency (
    currency_id SERIAL PRIMARY KEY,
    currency_code VARCHAR(3),
    created_at TIMESTAMP,
    last_updated TIMESTAMP
);

INSERT INTO currency
(currency_code, created_at, last_updated)
VALUES
('GBP', '1999-01-08 04:05:06', '1999-01-08 04:05:06'),
('EUR', '2024-02-14 09:00:00', '2024-02-14 09:00:00'),
('USD', '1999-01-08 04:05:06', '2024-02-14 09:00:00'),
('AUD', '2024-02-14 09:00:00', '1999-01-08 04:05:06');