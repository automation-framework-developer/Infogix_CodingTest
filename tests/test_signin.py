from pages.sign_in import SigninPage
import unittest
import pytest
import time
from utilities.teststatus import TestStatus
@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class SigninTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self,oneTimeSetUp):
        self.ts = TestStatus(self.driver)

    def test_signin(self):
        self.sign_in= SigninPage(self.driver)
        self.sign_in.clickSigninButton()
        result=self.sign_in.getTitle()
        self.ts.mark(result,"clicking on Sign in button user is redirected to login page")
        self.ts.markFinal("test_signinPage",result,"Sign in test case passed")

