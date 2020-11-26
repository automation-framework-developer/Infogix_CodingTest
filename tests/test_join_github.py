from pages.join_github import CreateAccountPage
from pages.sign_in import SigninPage
import unittest
import pytest
import time


from utilities.teststatus import TestStatus
@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class CreateAccountTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.ts = TestStatus(self.driver)
        self.signin = SigninPage(self.driver)
        self.createaccount= CreateAccountPage(self.driver)

    @pytest.mark.run(order=1)
    def test_checktext_githubpage(self):
        self.signin.clickSignupButton()
        result = self.createaccount.verifyCreateAccountText()
        self.ts.mark(result,"Text_Exists")
        self.ts.markFinal("test_checktext_githubpage",result,"Test Case Passed")

    @pytest.mark.run(order=2)
    def test_CreateAccountGreyedButton(self):
#        self.signin.clickSignupButton()
        self.createaccount.enterDetails(username="abcd51423",email="chandransh41@gmail.com",password="Chandransh@34")
        result = self.createaccount.checkCreateAccountButton()
        self.ts.mark(result, "Button_Greyed_out")
        self.ts.markFinal("test_CreateAccountGreyedButton", result, "Test Case Passed as button is greyed out")
