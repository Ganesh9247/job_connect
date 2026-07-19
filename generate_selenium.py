import os

base_dir = "qa-automation/src/test/java/com/jobconnect/qa"
files = {
    "base/BaseTest.java": """package com.jobconnect.qa.base;

import io.github.bonigarcia.wdm.WebDriverManager;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.annotations.AfterMethod;
import org.testng.annotations.BeforeMethod;

import java.time.Duration;

public class BaseTest {
    protected WebDriver driver;

    @BeforeMethod
    public void setUp() {
        WebDriverManager.chromedriver().setup();
        driver = new ChromeDriver();
        driver.manage().window().maximize();
        driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(10));
    }

    @AfterMethod
    public void tearDown() {
        if (driver != null) {
            driver.quit();
        }
    }
}
""",
    "pages/LoginPage.java": """package com.jobconnect.qa.pages;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;

public class LoginPage {
    private WebDriver driver;

    private By emailField = By.cssSelector("input[type='email']");
    private By passwordField = By.cssSelector("input[type='password']");
    private By loginButton = By.cssSelector("button[type='submit']");
    
    // In our actual implementation, the dashboard header indicates a successful login
    private By dashboardHeader = By.tagName("h2"); 

    public LoginPage(WebDriver driver) {
        this.driver = driver;
    }

    public void navigateToLogin(String baseUrl) {
        driver.get(baseUrl + "/login");
    }

    public void enterEmail(String email) {
        driver.findElement(emailField).sendKeys(email);
    }

    public void enterPassword(String password) {
        driver.findElement(passwordField).sendKeys(password);
    }

    public void clickLogin() {
        driver.findElement(loginButton).click();
    }

    public boolean isLoginSuccessful() {
        try {
            // Dashboard h2 text contains "Dashboard"
            WebElement header = driver.findElement(dashboardHeader);
            return header.getText().contains("Dashboard");
        } catch (Exception e) {
            return false;
        }
    }
}
""",
    "tests/LoginTest.java": """package com.jobconnect.qa.tests;

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
        
        // 4. Verify successful redirection to Dashboard
        Assert.assertTrue(loginPage.isLoginSuccessful(), "User was not redirected to the Dashboard after login.");
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
"""
}

for filepath, content in files.items():
    full_path = os.path.join(base_dir, filepath)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w") as f:
        f.write(content)

print("Selenium test classes generated successfully.")
