import requests


class TestWeworkApi:
    secrete = 'vZ_2MEw0qNpu1BazJh2ugialFgdykMiYwb_z_7ioHJg'
    id = 'ww299246c1085eb59a'

    def setup(self):
        r = requests.get(f'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={self.id}&corpsecret={self.secrete}')
        self.token = r.json()['access_token']
        # print(token)
        # r = requests.get(f'https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={token}&userid=ffsss')
        # print(r.json())

    def test_wework_api(self):
        # 获取成员
        r = requests.get(f'https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={self.token}&userid=ffsss')
        print(r.json())
        if r.json()['errcode'] == 0:
            requests.get(f'https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={self.token}&userid=ffsss')
            print(r.json())

        create_data = {
            'userid': 'wangshichong',
            'name': '王思聪',
            'mobile': '13000000000',
            'department': [1]
        }
        r = requests.post(f'https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.token}',
                          json=create_data)
        print(r.json())
        data = {
            'userid': 'wangshichong',
            'name': '王健林'
        }
        r = requests.post(f'https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.token}', json=data)
        print(r.json())
