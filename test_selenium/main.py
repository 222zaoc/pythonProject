import json
from time import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class Test:
    def setup(self):
        # 声明一个变量，设置为chromeoptions，
        chrome_opts = webdriver.ChromeOptions()
        # 设置chrome debugging代理，端口号保持一致 ：Google\ Chrome -remote-debugging-port=9222
        chrome_opts.debugger_address = "127.0.0.1:9222"
        # 打开一个复用的浏览器
        self.driver = webdriver.Chrome(options=chrome_opts)
        self.driver.get("https://work.weixin.qq.com/")
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    def test_test(self):
        # 获取cookies并给到变量
        cookies = self.driver.get_cookies()
        # 保存到文件  注：open之后，才可以读写
        with open("cookies.txt", 'w') as f:
            json.dump(cookies, f)
        # 读取文件
        with open("cookies.txt", "r") as f:
            cookies: list[dict] = json.load(f)
        for cookie in cookies:
            if "expiry" in cookie:
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)
        self.driver.get("http://work.weixin.qq.com/Wework_admin/frame#index")
