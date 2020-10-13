from test_appium.page.basepage import BasePage
from test_appium.page.impage import ImPage
# from test_appium.page.searchpage import SearchPage


class MessagePage(BasePage):
    def goto_search(self):
        self.steps("../yaml/search.yaml")
        from test_appium.page.searchpage import SearchPage
        return SearchPage(self._driver)

    def goto_im_single(self):
        return ImPage(self._driver)

    def goto_im_group(self):
        return ImPage(self._driver)

    def logout(self):
        from test_appium.page.main import Main
        return Main(self._driver)
