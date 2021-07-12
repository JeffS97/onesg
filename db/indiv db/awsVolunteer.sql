DROP DATABASE IF EXISTS awsVolunteer;
CREATE DATABASE awsVolunteer;
Use awsVolunteer;

CREATE TABLE awsVolunteer(
volunteer_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
volunter_name VARCHAR(200) NOT NULL,
username VARCHAR(200) NOT NULL,
email Varchar(200) NOT NULL,
address Varchar(200) NOT NULL,
chat_id VARCHAR(200) NOT NULL,

-- Stuff yall added in doc but not in the ss u sent me, @zhihao
sex VARCHAR(2) NULL,

-- hiya, who wrote this? care to explain? 
credentials VARCHAR(200) NOT NULL,

-- Added 3 properties
-- bio, postal code to use google api distance, matching interests with inititaive 
description VARCHAR(255) NULL,
dateOfBirth DATE NOT NULL,
postal_code INT NOT NULL,
areas_of_interest VARCHAR(255) NULL,

-- End of added properties
password Varchar(255) NOT NULL,
skills VARCHAR(250) NULL
);

