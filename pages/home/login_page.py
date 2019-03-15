from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver

class LoginPage(SeleniumDriver):

#posting this code to git repo so Shweta can refer it
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    _login_link = "Login"
    _email_field = "user_email"
    _password_field = "user_password"
    _login_button = "commit"

    #def getLoginLink(self):
    #    return self.driver.find_element(By.LINK_TEXT, self._login_link)

    #def getEmailField(self):
    #    return self.driver.find_element(By.ID, self._email_field)

    #def getPasswordField(self):
    #    return self.driver.find_element(By.ID, self._password_field)

    #def getLoginButton(self):
    #    return self.driver.find_element(By.NAME, self._login_button)

    #Actions (What we can do on above element)
    #def clickLoginLink(self):
      #  self.getLoginLink().click()

    def clickLoginLink(self):
        self.elementClick(self._login_link, locatorType="link")


    def enterEmail(self,email):
        #self.getEmailField().send_keys(email)
        self.sendKeys(email, self._email_field)

    def enterPassword(self, password):
        #self.getPasswordField().send_keys(password)
        self.sendKeys(password, self._password_field)

    def clickLoginButton(self):
        #self.getLoginButton().click()
        self.elementClick(self._login_button,locatorType= "name")


    def login(self, email, password):
        #loginLink = self.driver.find_element(By.LINK_TEXT, "Login")
        #loginLink.click()

        #emailField = self.driver.find_element(By.ID, "user_email")
        #emailField.send_keys(username)

        #passwordField = self.driver.find_element(By.ID, "user_password")
        #passwordField.send_keys(password)

        #loginButton = self.driver.find_element(By.NAME, "commit")
        #loginButton.click()

        self.clickLoginLink()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()

