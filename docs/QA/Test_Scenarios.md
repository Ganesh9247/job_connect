# Test Scenarios for JobConnect

A Test Scenario is a high-level functionality that can be tested. Below are the key test scenarios for the JobConnect application.

## TS_01: Authentication and Authorization
- **TS_01_01**: Verify that a user can register successfully with valid credentials.
- **TS_01_02**: Verify that a user cannot register with an existing email address.
- **TS_01_03**: Verify that a user can log in with valid credentials.
- **TS_01_04**: Verify that an invalid login attempt shows appropriate error messages.
- **TS_01_05**: Verify that users are redirected to their respective dashboards based on roles.
- **TS_01_06**: Verify that unauthenticated users cannot access protected routes (e.g., Dashboards, Admin panel).

## TS_02: Job Seeker Functionality
- **TS_02_01**: Verify that a Job Seeker can view the list of available jobs.
- **TS_02_02**: Verify that a Job Seeker can view details of a specific job.
- **TS_02_03**: Verify that a Job Seeker can apply to a job successfully.
- **TS_02_04**: Verify that a Job Seeker cannot apply to the same job multiple times.
- **TS_02_05**: Verify that a Job Seeker can upload a PDF resume.
- **TS_02_06**: Verify that a Job Seeker cannot upload non-PDF files for their resume.
- **TS_02_07**: Verify that a Job Seeker can view their applied jobs in the dashboard.

## TS_03: Search and Filter Functionality
- **TS_03_01**: Verify that a user can search for jobs using keywords (title/description).
- **TS_03_02**: Verify that a user can filter jobs by location.
- **TS_03_03**: Verify that a user can filter jobs by Job Type (e.g., Full Time, Remote).
- **TS_03_04**: Verify that a user can combine multiple filters successfully.
- **TS_03_05**: Verify the behavior when a search yields no results.

## TS_04: Recruiter Functionality
- **TS_04_01**: Verify that a Recruiter can post a new job with valid details.
- **TS_04_02**: Verify that a Recruiter can view a list of jobs they have posted.
- **TS_04_03**: Verify that a Recruiter can view applicants for a specific job.

## TS_05: Admin Functionality
- **TS_05_01**: Verify that an Admin can view all registered users.
- **TS_05_02**: Verify that an Admin can delete a user.
- **TS_05_03**: Verify that an Admin can view all job postings across the platform.
- **TS_05_04**: Verify that an Admin can delete a job posting.
- **TS_05_05**: Verify that standard users/recruiters cannot access the Admin dashboard.
