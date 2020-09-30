import time

from appium.webdriver.common.mobileby import MobileBy

from test_appium.page.basepage import BasePage
from test_appium.page.impage import ImPage
from test_appium.page.messagepage import MessagePage


class SearchPage(BasePage):
    def goto_im(self):
        return ImPage(self._driver)

    def goto_message(self):
        return MessagePage(self._driver)

    def im_single_search_result(self, value):
        self.send(value, MobileBy.ID, 'id')

    def search_result(self, value):
        self.send(value, MobileBy.ID, 'id')

    def im_group_search_result(self, value):
        self.send(value, MobileBy.ID, 'id')

    def address_book_search_result(self, value):
        self.send(value, MobileBy.ID, 'id')

    def selector_search_result(self, value):
        self.send(value, MobileBy.ID, 'id')
