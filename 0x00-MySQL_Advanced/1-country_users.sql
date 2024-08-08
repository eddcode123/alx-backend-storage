-- Script that creates a table users following these requirements:
-- id, email, name, country(enumeration of US, CO and TN)
CREATE TABLE IF NOT EXISTS users(
    id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email varchar(255) UNIQUE NOT NULL,
    name varchar(255)
    country ENUM('US', 'CO', 'TN')  DEFAULT 'US' NOT NULL
);
