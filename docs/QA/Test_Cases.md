# Test Cases for JobConnect

Below are detailed test cases derived from the Test Scenarios.

## Test Case 01: Job Seeker Registration
**Test Case ID**: TC_01_01
**Scenario**: TS_01_01 (Verify valid registration)
**Pre-conditions**: User is on the `/register` page.
**Test Steps**:
1. Enter valid Full Name (e.g., "John Doe").
2. Enter valid Email (e.g., "johndoe123@example.com").
3. Enter valid Password (e.g., "Password@123").
4. Select Role as "Job Seeker".
5. Click on the "Register" button.
**Expected Result**: System should show a success message "Registration successful" and redirect the user to the Login page.
**Actual Result**: (To be filled during execution)
**Status**: [PASS/FAIL]

## Test Case 02: Duplicate Email Registration
**Test Case ID**: TC_01_02
**Scenario**: TS_01_02
**Pre-conditions**: An account with `jobseeker@example.com` already exists.
**Test Steps**:
1. Enter Full Name "Test User".
2. Enter Email `jobseeker@example.com`.
3. Enter Password "password123".
4. Select any role.
5. Click "Register".
**Expected Result**: System should show an error message "Email is already taken!" and stay on the registration page.
**Actual Result**: (To be filled during execution)
**Status**: [PASS/FAIL]

## Test Case 03: Apply to a Job
**Test Case ID**: TC_02_03
**Scenario**: TS_02_03
**Pre-conditions**: Job seeker is logged in and is viewing a Job Details page for a job they haven't applied to.
**Test Steps**:
1. Click the "Apply Now" button.
**Expected Result**: System displays an alert "Applied successfully!" and the application appears in the Job Seeker's Dashboard.
**Actual Result**: (To be filled during execution)
**Status**: [PASS/FAIL]

## Test Case 04: Upload Invalid Resume Format
**Test Case ID**: TC_02_06
**Scenario**: TS_02_06
**Pre-conditions**: Job Seeker is logged into their Dashboard.
**Test Steps**:
1. Click on "Upload Resume".
2. Select a `.docx` or `.jpg` file from the file explorer.
3. Observe the system response.
**Expected Result**: System should reject the file and display an error message: "Please select a PDF file."
**Actual Result**: (To be filled during execution)
**Status**: [PASS/FAIL]

## Test Case 05: Admin Access Restriction
**Test Case ID**: TC_05_05
**Scenario**: TS_05_05
**Pre-conditions**: User is logged in as a Job Seeker or Recruiter.
**Test Steps**:
1. Attempt to manually navigate to the `/recruiter` or `/admin` routes.
2. Attempt to make a GET request to `/api/admin/users` via Postman using the Job Seeker's JWT token.
**Expected Result**: 
- Frontend should redirect or show a 403 Forbidden / Not Authorized page.
- Backend should return a `403 Forbidden` HTTP status code.
**Actual Result**: (To be filled during execution)
**Status**: [PASS/FAIL]
