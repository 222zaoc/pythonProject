import requests

from test_requests.api.wework import WeWork


class TestWeWork:
    secret = 'vZ_2MEw0qNpu1BazJh2ugialFgdykMiYwb_z_7ioHJg'

    def test_wework(self):
        print(WeWork().get_token(self.secret))
