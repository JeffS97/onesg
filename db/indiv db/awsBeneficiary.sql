DROP DATABASE IF EXISTS awsBeneficiary;
CREATE DATABASE awsBeneficiary;
Use awsBeneficiary;

CREATE TABLE awsBeneficiary(
beneficiary_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
beneficiary_name VARCHAR(200) NOT NULL,
username VARCHAR(200) NOT NULL,
email Varchar(200) NOT NULL,
address Varchar(200) NOT NULL,
sex VARCHAR(2) NULL,
description VARCHAR(255) NULL,
dateOfBirth DATE NOT NULL,
postal_code INT NOT NULL,
password Varchar(255) NOT NULL
);

