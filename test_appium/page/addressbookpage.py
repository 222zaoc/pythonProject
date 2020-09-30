from test_appium.page.basepage import BasePage
from test_appium.page.searchpage import SearchPage


class AddressBookPage(BasePage):
    def goto_search(self):
        return SearchPage(self._driver)
