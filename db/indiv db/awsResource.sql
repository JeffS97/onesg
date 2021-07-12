DROP DATABASE IF EXISTS awsResource;
CREATE DATABASE awsResource;
Use awsResource;

CREATE TABLE awsResource(
event_id INT NOT NULL,
-- I was thinking we should get users to select from a list as much as possible
-- This includes people and money 'people' & 'money'
resource_name VARCHAR(255) NOT NULL,

resource_qty INT NOT NULL,
resource_description VARCHAR(255) NULL,

PRIMARY KEY (event_id, resource_name)
);