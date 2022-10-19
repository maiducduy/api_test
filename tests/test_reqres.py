import requests, json


class Test:

    host_name = "https://reqres.in"
    def test_sample(self):
        api = "/api/users?page=2"
        url = Test.host_name + api
        res = requests.get(url=url, timeout=2)

        data = res.json()

        assert data["page"] == 2

    def test_create_new_user(self):
        api = "/api/users"
        data = {"name": "Duy Mai",
                "job": "Tester",
                "age": 36}
        url = Test.host_name + api
        res = requests.post(url=url,
                            json=data,
                            timeout=2)
        assert res.status_code == 201
        assert res.json()["name"] == "Duy Mai"
        assert "id" in res.json().keys()
