-- sample-data.sql
USE jobconnect_db;

-- Passwords are 'password123' hashed with BCrypt (10 rounds)
-- Hash: $2a$10$slYQmyNdGzTn7Z0SQq2HWeA/G4c4bV4FhM6FwT4kFmB4R4kE4D/mO

INSERT INTO users (id, full_name, email, phone, password, role) VALUES
(1, 'Admin User', 'admin@example.com', '1234567890', '$2a$10$QDqINMAPT0AvkMUlwYOn3eIgVCIZW4EjK19g8b1.VwpKeND8ou38G', 'ROLE_ADMIN'),
(2, 'Tech Recruiter', 'recruiter@example.com', '9876543210', '$2a$10$QDqINMAPT0AvkMUlwYOn3eIgVCIZW4EjK19g8b1.VwpKeND8ou38G', 'ROLE_RECRUITER'),
(3, 'John Doe', 'jobseeker@example.com', '5551234567', '$2a$10$QDqINMAPT0AvkMUlwYOn3eIgVCIZW4EjK19g8b1.VwpKeND8ou38G', 'ROLE_JOB_SEEKER'),
(4, 'Global Recruiter', 'recruiter2@example.com', '9876543211', '$2a$10$QDqINMAPT0AvkMUlwYOn3eIgVCIZW4EjK19g8b1.VwpKeND8ou38G', 'ROLE_RECRUITER');

INSERT INTO job_seeker_profiles (user_id, title, experience, current_company, current_salary, expected_salary, notice_period) VALUES
(3, 'Senior Java Developer', 5.5, 'TechCorp', 120000, 150000, 30);

INSERT INTO recruiter_profiles (user_id, company_name, industry, company_size, website, headquarters, about) VALUES
(2, 'TechNova Solutions', 'Information Technology', '1000-5000', 'https://technovasolutions.com', 'San Francisco, CA', 'A leading tech company providing innovative solutions.'),
(4, 'Global Innovators', 'Software Engineering', '50-200', 'https://globalinnovators.com', 'New York, NY', 'Startup focusing on AI and Machine Learning.');

INSERT INTO skills (id, name) VALUES
(1, 'Java'),
(2, 'Spring Boot'),
(3, 'React'),
(4, 'SQL'),
(5, 'JavaScript'),
(6, 'Manual Testing'),
(7, 'Selenium'),
(8, 'Python'),
(9, 'AWS'),
(10, 'Docker');

INSERT INTO user_skills (user_id, skill_id) VALUES
(3, 1), (3, 2), (3, 4), (3, 10);

INSERT INTO jobs (id, recruiter_id, title, location, description, responsibilities, requirements, min_experience, max_experience, min_salary, max_salary, job_type, work_mode, openings, deadline, status) VALUES
(1, 2, 'Senior Full Stack Developer', 'San Francisco, CA', 'Looking for an experienced full-stack developer.', 'Develop and maintain web applications.', 'Experience with React and Spring Boot.', 5.0, 8.0, 130000, 160000, 'Full Time', 'Hybrid', 2, '2026-12-31', 'ACTIVE'),
(2, 2, 'Java Backend Engineer', 'Remote', 'Join our core backend team.', 'Design and implement RESTful APIs.', 'Strong knowledge of Java, Spring, and SQL.', 3.0, 6.0, 110000, 140000, 'Full Time', 'Remote', 5, '2026-11-30', 'ACTIVE'),
(3, 2, 'QA Tester (Manual)', 'New York, NY', 'Looking for a meticulous QA tester.', 'Perform manual testing, write test cases.', 'Understanding of QA methodologies.', 1.0, 3.0, 60000, 80000, 'Full Time', 'On-site', 1, '2026-10-15', 'ACTIVE'),
(4, 4, 'React Frontend Developer', 'Remote', 'Frontend developer to build beautiful UIs.', 'Implement designs using React.', 'Strong React and CSS skills.', 2.0, 5.0, 90000, 120000, 'Full Time', 'Remote', 3, '2026-12-01', 'ACTIVE'),
(5, 4, 'Software Engineering Intern', 'San Francisco, CA', 'Summer internship.', 'Assist in software development.', 'Basic programming knowledge.', 0.0, 1.0, 30000, 40000, 'Internship', 'On-site', 5, '2026-08-31', 'ACTIVE');

-- Note: In a real scenario, we would seed 15-20 jobs, but this provides a starting point.
-- We can add more jobs dynamically via API.

INSERT INTO job_skills (job_id, skill_id) VALUES
(1, 1), (1, 2), (1, 3), (1, 4),
(2, 1), (2, 2), (2, 4),
(3, 6), (3, 4),
(4, 3), (4, 5),
(5, 1), (5, 5);

INSERT INTO applications (job_id, user_id, expected_salary, notice_period, status) VALUES
(1, 3, 140000, 30, 'APPLIED');

INSERT INTO saved_jobs (user_id, job_id) VALUES
(3, 2), (3, 4);
