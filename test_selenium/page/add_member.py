from selenium.webdriver.common.by import By

from test_selenium.page.base_page import BasePage


class AddMember(BasePage):
    def add_memeber(self):
        # def wait(driver):
        #     ele_len = len(self.finds(By.ID, "username"))
        #     if ele_len < 1:
        #         self.find(By.CSS_SELECTOR, ".js_has_member>div:nth-child(1) .js_add_member").click()
        #     # 如果username存在，就返回true
        #     return ele_len >= 1
        self.wait_for(By.ID, "asa")
        self.find(By.ID, "username").send_keys('abcde')
        self.find(By.ID, "memberAdd_acctid").send_keys('affff')
        self.find(By.ID, "memberAdd_phone").send_keys('12121211')
        # 点击保存
        self.find(By.CSS_SELECTOR, '.js_btn_save').click()

    def get_names(self):
        # 找出符合要求的所有element
        elems = self.finds(By.CSS_SELECTOR, "#member_list td:nth-cjild(2)")
        arrs = []
        # 对所有element进行遍历
        for elem in elems:
            # 依次取出其中的title属性，并存入数组
            arrs.append(elem.get_attribute("title"))
        return arrs
