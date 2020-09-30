import logging

import yaml
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver


class BasePage:
    logging.basicConfig(level=logging.INFO)
    _black_list = [(MobileBy.XPATH, "//*[@text='确定']"),
                   (MobileBy.XPATH, "//*[@text='允许']")]
    _error_num = 0
    _error_max = 3
    _params = {}

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    def find(self, by, locator=None):
        logging.info(by, locator)
        try:
            return self._driver.find_element(*locator) if isinstance(locator, tuple) else self._driver.find_element(
                by, locator)
        except Exception as e:
            if self._error_num > self._error_max:
                raise e
            self._error_num += 1
            # 处理弹窗
            for ele in self._black_list:
                elelist = self._driver.find_elements(*ele)
                if len(elelist) > 0:
                    elelist[0].click()
                    self.find(by, locator)
            raise e

    def finds(self, by, locator=None):
        logging.info(by, locator)
        try:
            return self._driver.find_elements(*locator) if isinstance(locator, tuple) else self._driver.find_elements(
                by, locator)
        except Exception as e:
            if self._error_num > self._error_max:
                raise e
            self._error_num += 1
            # 处理弹窗
            for ele in self._black_list:
                elelist = self._driver.find_elements(*ele)
                if len(elelist) > 0:
                    elelist[0].click()
                    self.finds(by, locator)
            raise e

    def send(self, value, by, locator=None):
        try:
            self.find(by, locator).send_keys(value)
        except Exception as e:
            if self._error_num > self._error_max:
                raise e
            self._error_num += 1
            for ele in self._black_list:
                elelist = self._driver.find_elements(*ele)
                if len(elelist) > 0:
                    elelist[0].click()
                    self.send(value, by, locator)
            raise e

    def steps(self, file):
        with open(file, encoding="utf-8") as f:
            steps: list[dict] = yaml.safe_load(f)
            for step in steps:
                logging.info(step)
                if 'by' in step.keys():
                    myby = step['by']
                    if myby == 'id':
                        element = self.find(step['by'], step['locator'])
                    if myby == 'xpath':
                        element = self.find(MobileBy.XPATH, step['locator'])
                if 'action' in step.keys():
                    action = step['action']
                    if action == 'click':
                        element.click()
                    elif action == 'send':
                        content: str = step['value']
                        for param in self._params:
                            content = content.replace(f"{param}", self._params[param])
                            self.send(content, step["by"], step["locator"])
