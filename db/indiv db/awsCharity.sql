DROP DATABASE IF EXISTS awsCharity;
CREATE DATABASE awsCharity;
Use awsCharity;

CREATE TABLE awsCharity(
charity_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
charity_name VARCHAR(200) NOT NULL,
c_username VARCHAR(200) NOT NULL,
c_email Varchar(200) NOT NULL,
password Varchar(255) NOT NULL,
-- chat_id VARCHAR(200) NOT NULL,

-- Added These
address Varchar(200) NOT NULL,
postal_code INT NULL,
beneficiary_type VARCHAR(255) NULL
);