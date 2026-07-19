package com.jobconnect.qa.pages;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;

public class LoginPage {
    private WebDriver driver;

    private By emailField = By.cssSelector("input[type='email']");
    private By passwordField = By.cssSelector("input[type='password']");
    private By loginButton = By.cssSelector("button[type='submit']");
    
    // After login, the app redirects to the Home page containing this text
    private By homeHeader = By.xpath("//h1[contains(text(), 'Welcome to JobConnect')]"); 

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
            // Implicit wait will now wait up to 10s for the Home page h1 to appear
            WebElement header = driver.findElement(homeHeader);
            return header.isDisplayed();
        } catch (Exception e) {
            return false;
        }
    }
}
