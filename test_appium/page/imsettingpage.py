from test_appium.page.basepage import BasePage
from test_appium.page.searchpage import SearchPage


class ImSettingPage(BasePage):
    def goto_im(self):
        from test_appium.page.impage import ImPage
        return ImPage(self._driver)

    def goto_search(self):
        return SearchPage(self._driver)
