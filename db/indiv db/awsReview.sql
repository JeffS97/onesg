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
