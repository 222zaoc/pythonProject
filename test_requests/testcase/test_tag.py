import json

# from jsonpath import jsonpath
import pytest

from test_requests.api.base_api import BaseApi
from test_requests.api.tag import Tag


class TestTag:
    test_data = BaseApi.load('test_tag_data.yaml')

    @classmethod
    def setup_class(cls):
        cls.tag = Tag()
        for name in ['add demo']:
            tag_id = cls.tag.jsonpath(cls.tag.get(), f'$..tag[?(@.name=="{name}")].id')
            if tag_id:
                cls.tag.delete(tag_id=tag_id[0])

    def setup(self):
        pass

    @pytest.mark.parametrize("name_old", "name_new", test_data)
    def test_all(self, name_old, name_new):
        assert self.tag.add(tag_name=name_old)['errcode'] == 0
        tag_id = self.tag.jsonpath(self.tag.get(), f'$..tag[?(@.name=="{name_old}")].id')[0]
        assert self.tag.update(tag_id, f'{name_new}')['errcode'] == 0

    def test_get(self):
        print(json.dumps(self.tag.get(), indent=2))

    def test_delete(self):
        self.tag.delete('dsfdfgfds')

    def test_add(self):
        assert self.tag.add(tag_name="add demo")['errcode'] ==0

    def test_update(self):
        self.tag.update('dasdsa', 'dsad')
