from selenium import webdriver

class WebdriverFactory:
    def __init__(self,browser):
        self.browser=browser

    def getWebDriverInstance(self):
        baseURL = 'https://github.com/'
        if self.browser == 'firefox':
            driver=webdriver.Firefox(executable_path=r"C:\Chandransh\Pycharm_Projects\Infogix_CodingTest\driver\geckodriver.exe")
        elif self.browser == "iexplorer":
            driver=webdriver.Ie(executable_path=r"C:\Chandransh\Pycharm_Projects\Infogix_CodingTest\driver\IEDriverServer.exe")
        elif self.browser == "chrome":
            driver=webdriver.Chrome(executable_path=r"C:\Chandransh\Pycharm_Projects\Infogix_CodingTest\driver\chromedriver.exe")
        else:
            driver=webdriver.Chrome(executable_path=r"C:\Chandransh\Pycharm_Projects\Infogix_CodingTest\driver\chromedriver.exe")

        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)
        return driver