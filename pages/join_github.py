from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging

class CreateAccountPage(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    #Locators
    _createaccount_text="//h1[contains(text(),'Create your account')]"
    _username="user_login"
    _emailaddress="user_email"
    _password="user_password"
    _createaccount_button="//*[@type='submit']"

    def enterUsername(self,username):
        self.sendKeys(username,self._username,locatorType="id")

    def enterEmail(self,email):
        self.sendKeys(email,self._emailaddress,locatorType="id")

    def enterPassword(self,password):
        self.sendKeys(password,self._password,locatorType="id")

    def checkCreateAccountButton(self):
        result = self.isElementEnabled(self._createaccount_button,locatorType="xpath")
        if result:
            result = False
            return result
        elif not result:
            result = True
            return result
        else:
            return True

    def enterDetails(self,username,email,password):
        self.enterUsername(username)
        self.enterEmail(email)
        self.enterPassword(password)


    def verifyCreateAccountText(self):
        text = self.getText(self._createaccount_text,locatorType="xpath")
        if text == "Create your account":
            self.log.info("Text exists")
            return True
        else:
            self.log.info("Text does not exist")
            return False

