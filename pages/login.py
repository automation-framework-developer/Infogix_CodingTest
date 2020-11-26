from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging
import time

class LoginPage(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    #Locators
    _username_textbox="login_field"
    _password_textbox="password"
    _signin_button="commit"
    _error_message="//*[@class='container-lg px-2' ]"
    _forgot_password="//a[contains(text(),'Forgot password?')]"

    def enterUsername(self,data):
        self.sendKeys(data,self._username_textbox,locatorType="id")

    def enterPassword(self,data):
        self.sendKeys(data,self._password_textbox,locatorType="id")

    def clickSignin(self):
        self.elementClick(self._signin_button,locatorType="name")

    def enterOnlyUsername(self):
        self.enterUsername("abc@gmail.com")
        self.clickSignin()
        time.sleep(2)

    def enterOnlyPassword(self):
        self.clearText(self._username_textbox,locatorType="id")
        self.enterPassword("abcd@123")
        self.clickSignin()
        time.sleep(2)

    def verifyErrorMessage(self):
        message=self.getText(self._error_message,locatorType="xpath")
        if message == "Incorrect username or password.":
            self.log.info("Text exists")
            return True
        else:
            self.log.info("Text does not exists")
            return False

    def clickForgotPassword(self):
        self.elementClick(self._forgot_password,locatorType="xpath")

