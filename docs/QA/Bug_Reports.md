# Bug Reports

*(This is a template to document bugs found during the manual testing phase of the JobConnect application.)*

## Bug 01: Example Bug Template
**Bug ID**: BR_001
**Title**: Resume upload allows non-PDF files if extension is manipulated.
**Severity**: Medium
**Priority**: High
**Environment**: Windows 11, Chrome Version 115, React Frontend (localhost:5173), Spring Boot Backend (localhost:8080)
**Steps to Reproduce**:
1. Log in as a Job Seeker.
2. Navigate to the Dashboard.
3. Attempt to upload a `.jpg` file that has been manually renamed to `.pdf`.
4. Click Upload.
**Expected Result**: The backend should validate the actual MIME type/file content and reject the fake PDF.
**Actual Result**: The file uploads successfully and the database stores the path.
**Attachment**: (Link to screenshot/video)
**Status**: Open

---

*(Testers should copy the template above to report actual bugs discovered during testing.)*
