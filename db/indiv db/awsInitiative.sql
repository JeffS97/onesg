DROP DATABASE IF EXISTS awsInitiative;
CREATE DATABASE awsInitiative;
Use awsInitiative;

CREATE TABLE awsInitiative(
initiative_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
initiative_name VARCHAR(200) NOT NULL,
description VARCHAR(255) NULL,
category VARCHAR(255) NULL,

-- If Volunteers and Chairities support / propose them
volunteer_id INT NOT NULL,
charity_id INT NULL, 

-- Will this suffice? Do we need to store which userId liked the initiative?
support INT NULL,
volunteer_goal INT NOT NULL,
donation_goal INT NOT NULL,

-- Tags: This refers Elderly, Children, Animals, Special Needs (and anything else)
-- Question, should I put this under Event or Initiative
beneficiary_type VARCHAR(255) NULL,

-- Tagging: Question, should I put this under Event or Initiative
skills_required VARCHAR(255) NULL,
date VARCHAR(255) NOT NULL,
current_donations INT NULL,
time VARCHAR(255) NOT NULL,
endorsed BOOLEAN NOT NULL
);
