# JobConnect – Job Portal Web Application

## Project Overview
JobConnect is a professional, full-stack job portal web application designed to connect job seekers with recruiters. It is built using a modern technology stack, ensuring scalability, security, and a responsive user experience. 
This project also serves as a robust foundation for Manual Testing, SQL Validation, and Automation Testing (Selenium) portfolios, containing realistic business logic and edge cases.

## Features
- **Job Seekers:** Browse jobs, search by keywords/location, view job details, apply for jobs, and manage applications in a dashboard.
- **Recruiters:** Create company profiles, post jobs, view posted jobs, and manage applicant statuses.
- **Authentication:** Secure JWT-based authentication with BCrypt password hashing and role-based access control (Job Seeker, Recruiter, Admin).
- **Modern UI:** Clean, responsive, and professional UI built with React.js and CSS3.

## Technology Stack
- **Frontend:** React.js, JavaScript, HTML5, CSS3, Axios, React Router (Vite).
- **Backend:** Java 17, Spring Boot 3+, Spring Data JPA, Spring Security, REST APIs, Maven.
- **Database:** MySQL.

## Architecture
The application follows a Clean Architecture approach with a strict separation of concerns:
- **Backend Layers:** Controller -> Service -> Repository -> Entity. 
- **Frontend Structure:** Pages, Components, Context, Services.
- **Security:** Stateless JWT authentication.

## Roles
- `ROLE_JOB_SEEKER`: Can browse, save, and apply for jobs.
- `ROLE_RECRUITER`: Can post jobs and manage applicants for their jobs.
- `ROLE_ADMIN`: Has overarching administrative privileges.

## Screenshots
*(Add screenshots here after deploying)*

## Installation & Setup

### Database Setup
1. Ensure MySQL Server is installed and running.
2. Open MySQL CLI or a UI tool like MySQL Workbench.
3. Execute the scripts located in the `database/` folder:
   ```sql
   source database/schema.sql;
   source database/sample-data.sql;
   ```

### Backend Setup
1. Navigate to the `backend/` directory.
2. Ensure you have Java 17+ and Maven installed.
3. Update `application.properties` with your MySQL credentials if they differ from root/root.
4. Run the Spring Boot application:
   ```bash
   ./mvnw spring-boot:run
   ```
   The backend will start on `http://localhost:8080`.

### Frontend Setup
1. Navigate to the `frontend/` directory.
2. Ensure Node.js is installed.
3. Install dependencies:
   ```bash
   npm install
   ```
4. Start the React development server:
   ```bash
   npm run dev
   ```
   The frontend will start on `http://localhost:5173`.

## Demo Accounts
Sample accounts are pre-seeded in the database for testing purposes. All passwords are `password123`.

- **Admin:** `admin@example.com`
- **Recruiter:** `recruiter@example.com`
- **Job Seeker:** `jobseeker@example.com`

## Project Structure
```
jobconnect/
├── backend/            # Spring Boot application
├── frontend/           # React application
├── database/           # SQL schema and seed data scripts
├── docs/               # Testing documentation
└── README.md
```

## Testing Strategy (Manual & Automation)
The application is designed to be highly testable, covering scenarios such as:
- **Authentication & Authorization:** Testing JWT generation, expiration, and role constraints.
- **CRUD Operations:** Posting jobs, applying to jobs, updating statuses.
- **Validations:** Edge cases for salary ranges, experience, and required fields.
- **Database Integrity:** Foreign key constraints, unique emails, and cascading deletes.
