from pages.login import LoginPage
from pages.sign_in import SigninPage
from pages.reset_password import ResetPasswordPage
import unittest
import pytest
import time
from utilities.teststatus import TestStatus
@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class ResetPasswordTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self,oneTimeSetUp):
        self.ts = TestStatus(self.driver)
        self.login = LoginPage(self.driver)
        self.signin = SigninPage(self.driver)
        self.reset = ResetPasswordPage(self.driver)

    @pytest.mark.run(order=1)
    def test_resetpassword_invalidemail(self):
        self.signin.clickSigninButton()
        self.login.clickForgotPassword()
        self.reset.invalidEmail()
        result = self.reset.verifyInvalidEmailText()
        self.ts.mark(result,"Invalid_email")
        self.ts.markFinal("test_resetpassword_invalidemail",result,"Inserting m.ie into email field in reset_password page displays error message")

    @pytest.mark.run(order=2)
    def test_resetpassword_emptyemail(self):
        self.reset.emptyVaueEmailField()
        result= self.reset.verifyInvalidEmailText()
        self.ts.mark(result, "Invalid_email_emptyValue")
        self.ts.markFinal("test_resetpassword_invalidemail", result,"Invalid email error when empty value is passed")
        result = self.reset.checkMessageFirstWord()
        self.ts.mark(result, "First_Word_check")
        self.ts.markFinal("test_resetpassword_emptyemail",result,"Test Case for checking first word Passed")

