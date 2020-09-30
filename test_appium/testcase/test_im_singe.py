from test_appium.page.app import App


class TestImSinge:
    def setup_class(self):
        self.message = App().start().main().goto_message()

    def setup(self):
        self.im_single = self.message.goto_im_single()

    def test_search_history(self):
        self.im_single.goto_im_setting().goto_search()
