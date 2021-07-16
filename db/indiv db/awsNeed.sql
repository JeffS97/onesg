DROP DATABASE IF EXISTS awsNeed;
CREATE DATABASE awsNeed;
Use awsNeed;

CREATE TABLE awsNeed(
beneficiary_id INT NOT NULL,
need_name VARCHAR(255) NOT NULL,

PRIMARY KEY (beneficiary_id, need_name)
);