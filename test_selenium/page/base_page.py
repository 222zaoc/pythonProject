from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

# 封装driver有关的操作
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    # 把driver提取出来
    _driver = ""
    base_url = ""

    def __init__(self, reuse=False):
        if reuse is True:
            # 如果driver为空调试模式开启本地9222调试
            chrome_opts = webdriver.ChromeOptions()
            # 设置chrome debugging代理，端口号保持一致 ：Google\ Chrome -remote-debugging-port=9222
            chrome_opts.debugger_address = "127.0.0.1:9222"
            # 打开一个复用的浏览器
            self._driver = webdriver.Chrome(options=chrome_opts)
        else:
            # 打开一个新的浏览器
            self.driver = webdriver.Chrome()
        if self.base_url != "":
            self._driver.get(self.base_url)
        # 隐式等待，解决元素加载过慢的问题
        self.driver.implicitly_wait(3)

    def find(self, locator, value):
        return self.driver.find_element(locator, value)

    def finds(self, locator, value):
        return self.driver.find_elements(locator, value)

    # 显示等待
    def wait_for(self, locator, value):
        # WebDriverWait(self._driver).until(fun)
        WebDriverWait(self._driver, 10).until(expected_conditions.element_to_be_clickable((locator, value)))

    def quit(self):
        return self._driver.quit()
