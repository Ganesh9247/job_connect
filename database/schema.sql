-- schema.sql
CREATE DATABASE IF NOT EXISTS jobconnect_db;
USE jobconnect_db;

CREATE TABLE users (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    phone VARCHAR(20),
    password VARCHAR(255) NOT NULL,
    role VARCHAR(20) NOT NULL, -- ROLE_JOB_SEEKER, ROLE_RECRUITER, ROLE_ADMIN
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE job_seeker_profiles (
    user_id BIGINT PRIMARY KEY,
    title VARCHAR(100),
    experience DECIMAL(4,2), -- Years of experience
    current_company VARCHAR(100),
    current_salary DECIMAL(12,2),
    expected_salary DECIMAL(12,2),
    notice_period INT, -- In days
    resume_url VARCHAR(255),
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

CREATE TABLE recruiter_profiles (
    user_id BIGINT PRIMARY KEY,
    company_name VARCHAR(100) NOT NULL,
    logo_url VARCHAR(255),
    industry VARCHAR(100),
    company_size VARCHAR(50),
    website VARCHAR(255),
    headquarters VARCHAR(100),
    about TEXT,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

CREATE TABLE skills (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE user_skills (
    user_id BIGINT,
    skill_id BIGINT,
    PRIMARY KEY (user_id, skill_id),
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (skill_id) REFERENCES skills(id) ON DELETE CASCADE
);

CREATE TABLE jobs (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    recruiter_id BIGINT NOT NULL,
    title VARCHAR(100) NOT NULL,
    location VARCHAR(100),
    description TEXT,
    responsibilities TEXT,
    requirements TEXT,
    min_experience DECIMAL(4,2),
    max_experience DECIMAL(4,2),
    min_salary DECIMAL(12,2),
    max_salary DECIMAL(12,2),
    job_type VARCHAR(50), -- Full Time, Part Time, Internship, Contract
    work_mode VARCHAR(50), -- On-site, Remote, Hybrid
    openings INT,
    deadline DATE,
    status VARCHAR(20) DEFAULT 'ACTIVE', -- DRAFT, ACTIVE, CLOSED, EXPIRED
    posted_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (recruiter_id) REFERENCES users(id) ON DELETE CASCADE
);

CREATE TABLE job_skills (
    job_id BIGINT,
    skill_id BIGINT,
    PRIMARY KEY (job_id, skill_id),
    FOREIGN KEY (job_id) REFERENCES jobs(id) ON DELETE CASCADE,
    FOREIGN KEY (skill_id) REFERENCES skills(id) ON DELETE CASCADE
);

CREATE TABLE applications (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    job_id BIGINT NOT NULL,
    user_id BIGINT NOT NULL,
    resume_url VARCHAR(255),
    cover_letter TEXT,
    expected_salary DECIMAL(12,2),
    notice_period INT,
    status VARCHAR(50) DEFAULT 'APPLIED', -- APPLIED, UNDER_REVIEW, SHORTLISTED, INTERVIEW_SCHEDULED, SELECTED, REJECTED, WITHDRAWN
    applied_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (job_id) REFERENCES jobs(id) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    UNIQUE KEY unique_application (job_id, user_id)
);

CREATE TABLE saved_jobs (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    user_id BIGINT NOT NULL,
    job_id BIGINT NOT NULL,
    saved_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (job_id) REFERENCES jobs(id) ON DELETE CASCADE,
    UNIQUE KEY unique_saved_job (user_id, job_id)
);
