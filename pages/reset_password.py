from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging
import time
class ResetPasswordPage(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    #Locators
    _emailaddress_textbox="//input[@id='email_field']"
    _resetemail_button="commit"
    _invalid_emailtext="//*[@class='container-lg px-2']"

    def enterEmailaddress(self,data):
        self.sendKeys(data,self._emailaddress_textbox,locatorType="xpath")

    def clickResetEmailButton(self):
        self.elementClick(self._resetemail_button,locatorType="name")

    def invalidEmail(self,data="m.ie"):
        self.enterEmailaddress(data)
        self.clickResetEmailButton()
        time.sleep(2)

    def emptyVaueEmailField(self):
        self.clickResetEmailButton()

    def verifyInvalidEmailText(self):
        text = self.getText(self._invalid_emailtext,locatorType="xpath")
        if text == "That address is not a verified primary email or is not associated with a personal user account. Organization billing emails are only for notifications":
            self.log.info("Text is present")
            return True
        else:
            self.log.info("Text is not present")
            return False

    def checkMessageFirstWord(self):
        text = self.getText(self._invalid_emailtext, locatorType="xpath")
        first_word= text.split()[0]
        if first_word == "That":
            self.log.info("First word extracted is {} and correct".format(first_word))
            return True
        else:

            self.log.info("First word extracted is incorrect")




