CREATE TABLE IF NOT EXISTS orders (
  order_id BIGSERIAL PRIMARY KEY,
  customer_name VARCHAR(50) NOT NULL,
  customer_id VARCHAR(50) NOT NULL,
  purchase_time TIMESTAMP NOT NULL DEFAULT current_timestamp
);

CREATE TABLE IF NOT EXISTS order_item (
	id BIGSERIAL PRIMARY KEY,
	order_id BIGINT NOT NULL,
	product_name VARCHAR(50) NOT NULL,
	amount INT NOT NULL,
	product_id VARCHAR(100) NOT NULL,
	price INT NOT NULL,
	CONSTRAINT fk_order
		FOREIGN KEY(order_id)
			REFERENCES orders(order_id)
			ON DELETE CASCADE
);
