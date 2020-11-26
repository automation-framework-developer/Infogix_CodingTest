from pages.login import LoginPage
from pages.sign_in import SigninPage
import unittest
import pytest
import time
from utilities.teststatus import TestStatus
@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self,oneTimeSetUp):
        self.ts = TestStatus(self.driver)

    def test_login(self):
        self.login= LoginPage(self.driver)
        self.signin= SigninPage(self.driver)
        self.signin.clickSigninButton()

        self.login.enterOnlyUsername()

        result=self.login.verifyErrorMessage()
        self.ts.mark(result,"Username_Mandatory_Field")
        self.login.enterOnlyPassword()

        result= self.login.verifyErrorMessage()
        self.ts.mark(result,"Password_Mandatory_Field")
        self.ts.markFinal("test_login",result,"Test Case passed for username and password as mandatory fields")

