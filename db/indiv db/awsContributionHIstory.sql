DROP DATABASE IF EXISTS awsContributionHistory;
CREATE DATABASE awsContributionHistory;
Use awsContributionHistory;

CREATE TABLE awsContributionHistory(
volunteer_id INT NOT NULL,
initiative_id INT NOT NULL,
resource_name VARCHAR(255) NOT NULL,
resource_qty INT NOT NULL,

-- Do we need this? (To record date and time of review)
date DATE NOT NULL,
time TIME NOT NULL
);