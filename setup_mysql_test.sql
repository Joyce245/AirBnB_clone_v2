-- create a data base, an User and give permises just for this data base and
-- SELECT permises
-- CREATE DATABASE AND USER
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- GIVE THE PRIVILEGES
USE hbnb_test_db;
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
