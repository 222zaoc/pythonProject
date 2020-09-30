from time import sleep

from test_selenium.page.index import Index


class TestMember:
    def setup(self):
        self.index = Index(reuse=True)

    def test_addmember(self):
        add_member = self.index.goto_addmember()
        # 添加成员
        add_member.add_memeber()
        sleep(2)
        # 测试是否添加
        assert 'asd' in add_member.get_names()
