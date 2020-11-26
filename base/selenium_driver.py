from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys
import utilities.custom_logger as cl
from selenium.webdriver.support.select import Select
import logging
import time
import os


class SeleniumDriver():
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        elif locatorType == "class":
            return By.CLASS_NAME
        else:
            self.log.info("Locator type" + locatorType + "is not correct/supported")
            return False

    def getElement(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            self.log.info("Element Found with locator type" + locatorType + "for locator" + locator)
        except:
            self.log.error("Element not Found with locator type" + locatorType + "for locator" + locator)
        return element

    def getElementList(self, locator, locatorType='id'):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_elements(byType, locator)
            self.log.info("Element list found with locator: " + locator + "and locator type" + locatorType)
        except:
            self.log.info("Element list not found with locator: " + locator + "and locator type" + locatorType)

    def getTitle(self):
        return self.driver.title

    def elementClick(self, locator=" ", locatorType="id", element=None):
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            element.click()
            self.log.info("Clicked on element with locator" + locator + "locatorType:" + locatorType)
        except:
            self.log.info("Cannot click on element with locator type" + locator + "locator Type:" + locatorType)
            print_stack()

    def sendKeys(self, data, locator, locatorType="id", element=None):
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            element.send_keys(data)
            self.log.info("Send data on element with locator" + locator + " locatorType:" + locatorType)
        except:
            self.log.info("Cannot send data on element with locator type" + locator + " locator Type:" + locatorType)
            print_stack()

    def pressEnter(self, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            element.send_keys(Keys.ENTER)
            self.log.info("Enter key pressed")
        except:
            self.log.info("Unable to press enter key")
            print_stack()

    def isElementPresent(self, locator="", locatorType="id", element=None):
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            if element is not None:
                self.log.info("Element present with locator: " + locator + "locatortype:" + locatorType)
                return True
            else:
                self.log.info("Element not found")
                return False
        except:
            self.log.info("Element not found")
            return False

    def elementPresenceCheck(self, locator, locatorType="id"):
        try:
            byType = self.getByType(locatorType)
            elementList = self.driver.find_elements(byType, locator)
            if len(elementList) > 0:
                self.log.info("Element Found")
                return True
            else:
                self.log.info("Element not found")
                return False
        except:
            self.log("Element not found")
            return False

    def waitForElement(self, locator, locatorType="id", timeout=10, poll_frequency=0.5):
        element = None
        try:
            byType = self.getByType(locatorType)
            self.log.info("Waiting for maximum::" + str(timeout) + ":: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, timeout=10, poll_frequency=1,
                                 ignored_exceptions=[NoSuchElementException, ElementNotVisibleException,
                                                     ElementNotSelectableException,
                                                     ElementNotInteractableException])
            element = wait.until(EC.element_to_be_clickable((byType, locator)))
            self.log.info("Element appeared on webpage")
        except:
            self.log.info("Element not appeared on webpage")
            print_stack()
        return element

    def screenShot(self, resultMessage):

        fileName = resultMessage + "." + str(round(time.time() * 1000)) + ".png"
        screenshotDirectory = "../screenshots/"
        relativeFileName = screenshotDirectory + fileName
        currentDirectory = os.path.dirname(__file__)
        destinationFile = os.path.join(currentDirectory, relativeFileName)
        destinationDirectory = os.path.join(currentDirectory, screenshotDirectory)

        try:
            if not os.path.exists(destinationDirectory):
                os.makedirs(destinationDirectory)

            self.driver.save_screenshot(destinationFile)
            self.log.info("ScreenShot saved to directory")

        except:
            self.log.error("### EXCEPTION OCCURED")
            print_stack()

    def getText(self, locator="", locatorType="id", element=None, info=""):

        try:
            if locator:  # This means if locator is not empty
                self.log.debug("In locator condition")
                element = self.getElement(locator, locatorType)
            self.log.debug("Before finding text")
            text = element.text
            self.log.debug("After finding element, size is: " + str(len(text)))
            if len(text) == 0:
                text = element.get_attribute("innerText")
            if len(text) != 0:
                self.log.info("Getting text on element :: " + info)
                self.log.info("The text is :: '" + text + "'")
                text = text.strip()
        except:
            self.log.error("Failed to get text on element " + info)
            print_stack()
            text = None
        return text

    def webScroll(self, direction="up"):

        if direction == "up":
            # Scroll Up
            self.driver.execute_script("window.scrollBy(0, -1000);")

        if direction == "down":
            # Scroll Down
            self.driver.execute_script("window.scrollBy(0, 1000);")

    def selectDropdown(self, locator="", locatorType="id", element=None, index="", value="", text=""):
        try:
            if locator:
                element = self.getElement(locator, locatorType)
                self.log.info("Element for select by value with" + locator + "/t found with" + locatorType)
            sel = Select(element)
            if index:
                self.log.info("Select value found by index")
                sel.select_by_index(index)

            elif value:
                self.log.info("Select value found by value")
                sel.select_by_value(value)

            elif text:
                self.log.info("Select value found by visible text")
                sel.select_by_visible_text(text)
            return True
        except:
            self.log.error("Value not found for select .Encountered exception")
            return False

    def wait_implicit(self,timeperiod):
        self.driver.implicitly_wait(timeperiod)
        self.log.info("Wait time is {} seconds".format(timeperiod))

    def compareTexts(self,expectedText,actualText):
        try:
            if actualText == expectedText:
                result = True
                self.log.info("Texts" + actualText + "matches with " + expectedText + "Test point is successfull")
                return result
            else:
                result = False
                self.log.info(
                    "Texts" + actualText + "does not matches with " + expectedText + "Test point is successfull")
        except:
            self.log.info(
                "Texts" + actualText + "does not matches with " + expectedText + "Test point is not successfull")
            return False

    def clearText(self, locator, locatorType="id", element=None):
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            element.clear()
            self.log.info("Data cleared on textbox " + locator + " locatorType:" + locatorType)
        except:
            self.log.info("Cannot clear the data on element with locator type" + locator + " locator Type:" + locatorType)
            print_stack()

    def isElementEnabled(self,locator,locatorType="id",element=None):
         try:
             if locator:
                element = self.getElement(locator, locatorType)
             status = element.is_enabled()
             self.log.info("Status is {}".format(status))
             if status == True:
                 self.log.info("Element is enabled for " + locator + " locatorType:" + locatorType)
                 return status
             else:
                 status = False
                 self.log.info("Element is disabled for selenium_driver" + locator + " locator Type:" + locatorType)
                 return status
         except:
             self.log.info("Element is disabled for selenium driver except block" + locator + " locator Type:" + locatorType)
             print_stack()
             return False

