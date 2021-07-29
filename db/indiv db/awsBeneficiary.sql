DROP DATABASE IF EXISTS awsBeneficiary;
CREATE DATABASE awsBeneficiary;
Use awsBeneficiary;

CREATE TABLE awsBeneficiary(
beneficiary_type VARCHAR(100) NOT NULL, 
beneficiary_name VARCHAR(200) NOT NULL,
username VARCHAR(200) PRIMARY KEY,
email Varchar(200) NOT NULL,
sex VARCHAR(20) NULL,
dateOfBirth DATE NOT NULL,
postal_code INT NOT NULL,
interest VARCHAR(255) NULL
);

