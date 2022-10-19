import requests


class Test:
    def test_sample(self):
        hostname = "https://reqres.in"
        api = "/api/users?page=2"
        url = hostname + api
        res = requests.get(url=url, timeout=2)

        data = res.json()

        assert data["page"] == 2
