show databases;
create database xcareers;
use xcareers;
CREATE TABLE applications (
  application_id INT PRIMARY KEY not null auto_increment,
  applier_name VARCHAR(255) NOT NULL,
  applier_email VARCHAR(255) NOT NULL,
  applier_linkedin_url VARCHAR(2000),
  applier_leetcode_url VARCHAR(2000),
  applier_education_detail VARCHAR(2000),
  applier_work_experience VARCHAR(2000),
  job_application_id INT NOT NULL,
  FOREIGN KEY (job_application_id) REFERENCES jobs (id)
);

 CREATE TABLE jobs (
     id INT NOT NULL auto_increment PRIMARY KEY,
     title VARCHAR(120) not null,
     location VARCHAR(150) not null,
     email VARCHAR(100),
     phone_number VARCHAR(12),
     address VARCHAR(2000),
     about varchar(2000),
     requirements varchar(2000),
     responsibilities varchar(2000),
     salary INT,
     created_at timestamp default current_timestamp,
    zip_code VARCHAR(10)
 );
INSERT INTO jobs (title, location, email, phone_number, address, about, requirements, responsibilities, salary, zip_code)
VALUES
('Project Manager', 'New York', 'pm@company.com', '123-456-7890', '2828 Broadway', 'Plan and oversee projects from start to finish', 'Bachelor degree in Project Management or related field, proficient in Microsoft Project and Excel, familiar with Agile and Scrum methodologies', 'Define project scope, objectives, and deliverables, create and manage project schedules and budgets, coordinate and communicate with project stakeholders and team members, monitor and control project quality and risks, report on project progress and outcomes', 80000, '10001')
;


SELECT *  FROM jobs WHERE MATCH(title, location, about, requirements, responsibilities) against('india');

INSERT INTO applications (
  applier_name,
  applier_email,
  applier_linkedin_url,
  applier_leetcode_url,
  applier_education_detail,
  applier_work_experience,
  job_application_id
) VALUES (
  'swarup shah',
  'john.doe@email.com',
  'https://www.linkedin.com/in/johndoe',
  'https://leetcode.com/johndoe',
  'Bachelor of Science in Computer Science',
  'Software Engineer at XYZ Corp',
  1
);


select * from applications;
-- UPDATE  user
-- SET first_name = 'swarup',
--     last_name = 'shah',
--     email = 'swarupshah03@hotmail.com',
--     phone_number = '6355494571',
--     address = '32, BL Soc.',
--     city = 'vadodara',
--     state = 'Gujarat',
--     zip_code = '390011'
-- WHERE id = 5;
