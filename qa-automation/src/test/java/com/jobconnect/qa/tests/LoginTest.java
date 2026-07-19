package com.jobconnect.qa.tests;

import com.jobconnect.qa.base.BaseTest;
import com.jobconnect.qa.pages.LoginPage;
import org.testng.Assert;
import org.testng.annotations.Test;

public class LoginTest extends BaseTest {

    private final String BASE_URL = "http://localhost:5173";

    @Test
    public void testValidJobSeekerLogin() {
        LoginPage loginPage = new LoginPage(driver);
        
        // 1. Navigate to login page
        loginPage.navigateToLogin(BASE_URL);
        
        // 2. Enter valid job seeker credentials (as seeded in database)
        loginPage.enterEmail("jobseeker@example.com");
        loginPage.enterPassword("password123");
        
        // 3. Click Login
        loginPage.clickLogin();
        
        // 4. Verify successful redirection to Home
        Assert.assertTrue(loginPage.isLoginSuccessful(), "User was not redirected to the Home page after login.");
    }
    
    @Test
    public void testInvalidLogin() {
        LoginPage loginPage = new LoginPage(driver);
        
        loginPage.navigateToLogin(BASE_URL);
        
        loginPage.enterEmail("wrong@example.com");
        loginPage.enterPassword("wrongpassword");
        
        loginPage.clickLogin();
        
        // Login should fail, so we should NOT see the dashboard
        Assert.assertFalse(loginPage.isLoginSuccessful(), "User was incorrectly logged in with bad credentials.");
    }
}
