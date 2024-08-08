-- Check if the table exists and create it if it doesn't with this fileds
-- id, email, name, country
CREATE TABLE IF NOT EXISTS users (
    id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email varchar(255) UNIQUE NOT NULL,
    name varchar(255)
    country ENUM('US', 'CO', 'TN')  DEFAULT 'US' NOt NULL
);
