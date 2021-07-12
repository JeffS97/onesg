DROP DATABASE IF EXISTS awsEvent;
CREATE DATABASE awsEvent;
Use awsEvent;

CREATE TABLE awsEvent(
event_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
initiative_id INT NOT NULL,

date DATE NOT NULL,
time TIME NOT NULL,

-- Could be Virtual, hence nullable
address VARCHAR(255) NULL,
postal_code INT NULL
);

