from test_appium.page.addressbookpage import AddressBookPage
from test_appium.page.basepage import BasePage
from test_appium.page.impage import ImPage
from test_appium.page.messagepage import MessagePage


class Main(BasePage):
    def goto_message(self):
        return MessagePage(self._driver)

    def goto_addresslist(self):
        return AddressBookPage(self._driver)

    def goto_im(self):
        return ImPage(self._driver)

    def login(self):
        return MessagePage(self._driver)
