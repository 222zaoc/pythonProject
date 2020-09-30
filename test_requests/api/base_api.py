from pprint import pprint
from string import Template

import requests
import yaml
from jsonpath import jsonpath


class BaseApi:

    def send_api(self, req: dict):
        # 使用request 完成多请求改造
        pprint(req)
        r = requests.request(**req)
        pprint(r.json())
        return r.json()

    @classmethod
    def jsonpath(cls, json, expr):
        return jsonpath(json, expr)

    @classmethod
    def load(cls, path):
        with open(path, 'r') as f:
            return yaml.safe_load(f)

    @classmethod
    def template(cls, path, data, sub=None):
        with open(path, 'r') as f:
            if sub is None:
                return yaml.load(Template(f.read()).substitute(data))
            else:
                return yaml.load(Template(yaml.load(f)[sub]).substitute(data))
