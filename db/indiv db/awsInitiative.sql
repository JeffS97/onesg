DROP DATABASE IF EXISTS awsIniative;
CREATE DATABASE awsIniative;
Use awsIniative;

CREATE TABLE awsInitiative(
initiative_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
initiative_name VARCHAR(200) NOT NULL,
description VARCHAR(255) NULL,

-- Will this suffice? Do we need to store which userId liked the initiative?
support INT NULL,

-- Tags: This refers Elderly, Children, Animals, Special Needs (and anything else)
-- Question, should I put this under Event or Initiative
beneficiary_type VARCHAR(255) NULL,

-- Tagging: Question, should I put this under Event or Initiative
skills_required VARCHAR(255) NULL
);
