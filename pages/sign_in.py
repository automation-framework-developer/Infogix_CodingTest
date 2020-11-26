from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging
import time
class SigninPage(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    #Locators
    _signin_button="//a[contains(text(),'Sign in')]"
    _signup_button="(//*[@type='submit' and contains(text(),'Sign up for GitHub')])[1]"

    def clickSigninButton(self):
#self.waitForElement(self._signin_button)
        self.elementClick(self._signin_button,locatorType="xpath")
        time.sleep(2)
    def clickSignupButton(self):
        self.elementClick(self._signup_button,locatorType="xpath")

    def verifyTitle(self):
        if self.getTitle() == 'Sign in to GitHub · GitHub':
            return True
        else:
            return False
