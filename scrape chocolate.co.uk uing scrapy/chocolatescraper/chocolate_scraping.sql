-- CREATE DATABASE chocolate_scraping;
USE chocolate_scraping;

CREATE TABLE chocolate_products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    url VARCHAR(255) NOT NULL
);

