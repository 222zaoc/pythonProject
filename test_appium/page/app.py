import os

from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from test_appium.page.basepage import BasePage
from test_appium.page.main import Main


class App(BasePage):
    _package = ""
    _activity = ""

    def start(self):

        if self._driver is None:
            caps = {}
            caps["platforName"] = "android"
            caps["deviceName"] = "6160a6b0"
            caps["appPackage"] = self._package
            caps["activity"] = self._activity
            caps["autoGrantPemissions"] = True
            caps["noReset"] = True
            # udid = os.getenv('udid')
            # caps["udid"] = udid
            # caps["chromedriverExecutable"] = ""
            # self._driver = webdriver.Remote("http://localhost:4444/wd/hub", caps)
            self._driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            self._driver.implicitly_wait(3)
        else:
            print("reuse")
            self._driver.start_activity(self._package, self._activity)
        return self

    def restart(self):
        self._driver.start_activity(self._package, self._activity)

    def main(self):
        return Main(self._driver)
