-- products table: holds each item you sell
CREATE TABLE IF NOT EXISTS products (
  product_id   INTEGER PRIMARY KEY,   -- unique ID per product
  name         TEXT,                  -- name of the product
  category     TEXT,                  -- e.g. Apparel, Electronics
  unit_price   REAL                   -- price per unit, e.g. 19.99
);

-- sales table: records each sale event
CREATE TABLE IF NOT EXISTS sales (
  sale_id      INTEGER PRIMARY KEY,             -- unique ID per sale record
  product_id   INTEGER REFERENCES products,     -- which product was sold
  sale_date    DATE,                            -- date of the sale
  quantity     INTEGER,                         -- how many units sold
  total_amount REAL                             -- quantity × unit_price
);
