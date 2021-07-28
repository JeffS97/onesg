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

DROP DATABASE IF EXISTS awsContributionHistory;
CREATE DATABASE awsContributionHistory;
Use awsContributionHistory;

CREATE TABLE awsContributionHistory(
volunteer_id INT NOT NULL,
event_id INT NOT NULL,
resource_name VARCHAR(255) NOT NULL,
resource_qty INT NOT NULL,

-- Do we need this? (To record date and time of review)
date DATE NOT NULL,
time TIME NOT NULL,

PRIMARY KEY (volunteer_id, event_id, resource_name)
);

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
time VARCHAR(255) NOT NULL
);

DROP DATABASE IF EXISTS awsResource;
CREATE DATABASE awsResource;
Use awsResource;

CREATE TABLE awsResource(
event_id INT NOT NULL,
-- I was thinking we should get users to select from a list as much as possible
-- This includes people and money 'people' & 'money'
resource_name VARCHAR(255) NOT NULL,

resource_qty_required INT NOT NULL,
resource_qty_obtained INT NOT NULL,
resource_description VARCHAR(255) NULL,

PRIMARY KEY (event_id, resource_name)
);

DROP DATABASE IF EXISTS awsReview;
CREATE DATABASE awsReview;
Use awsReview;

CREATE TABLE awsReview(
review_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
rating INT NOT NULL, 

-- This looks a bit dumb :/ Is there a better way to handle these?

-- from
volunteer_id INT NULL,
charity_id INT NULL,

-- to
to_volunteer_id INT NULL,
to_charity_id INT NULL,
to_initiative_id INT NULL,

-- To record date and time of review
date DATE NOT NULL,
time TIME NOT NULL
);

DROP DATABASE IF EXISTS awsVolunteer;
CREATE DATABASE awsVolunteer;
Use awsVolunteer;

CREATE TABLE awsVolunteer(
volunteer_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
volunteer_name VARCHAR(200) NOT NULL,
username VARCHAR(200) NOT NULL,
email Varchar(200) NOT NULL,
address Varchar(200) NOT NULL,
-- chat_id VARCHAR(200) NOT NULL,
payment VARCHAR(200) NOT NULL,

-- Stuff yall added in doc but not in the ss u sent me, @zhihao
sex VARCHAR(2) NULL,

-- hiya, who wrote this? care to explain? 
credentials VARCHAR(200) NOT NULL,

-- Added 3 properties
-- bio, postal code to use google api distance, matching interests with inititaive 
description VARCHAR(255) NULL,
age INT NOT NULL,
postal_code INT NOT NULL,
areas_of_interest VARCHAR(255) NULL,

-- End of added properties
password Varchar(255) NOT NULL,
skills VARCHAR(250) NULL
);

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

DROP DATABASE IF EXISTS awsNeed;
CREATE DATABASE awsNeed;
Use awsNeed;

CREATE TABLE awsNeed(
beneficiary_id INT NOT NULL,
need_name VARCHAR(255) NOT NULL,

PRIMARY KEY (beneficiary_id, need_name)
);