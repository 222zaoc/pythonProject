from pprint import pprint

import yaml


def test_load():
    with open("test_tag_data.yaml", 'r') as f:
        pprint(yaml.safe_load(f))
