from selenium import webdriver
from selenium.webdriver.common.by import By

from test_selenium.page.add_member import AddMember
from test_selenium.page.base_page import BasePage


class Index(BasePage):
    base_url = "https://work.weixin.qq.com/wework_admin/frame#index"

    def goto_addmember(self):
        # 点击添加成员按钮
        self.find(By.ID, "menu_contacts").click()
        # 跳转到添加成员页
        self.wait_for(By.ID, "username")
        return AddMember(reuse=True)

    def goto_import_address(self):
        pass

    def goto_member_join(self):
        pass
