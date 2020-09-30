import requests

from test_requests.api.base_api import BaseApi


class WeWork(BaseApi):
    corpid = 'ww299246c1085eb59a'

    # 获取token
    def get_token(self, secret):
        data = {
            'method': 'get',
            'url': 'https://qyapi.weixin.qq.com/cgi-bin/gettoken',
            'params': {
                'corpid': self.corpid,
                'corpsecret': secret
            }
        }
        return self.send_api(data)['access_token']
