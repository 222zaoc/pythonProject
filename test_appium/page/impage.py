from test_appium.page.basepage import BasePage
from test_appium.page.imsettingpage import ImSettingPage


class ImPage(BasePage):
    def goto_im_setting(self):
        return ImSettingPage(self._driver)
