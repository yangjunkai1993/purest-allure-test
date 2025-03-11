import requests
import pytest

token =""

def test_Login_admin():
    headers = {"Content-Type": "application/json; charset=utf-8"}
    login_data = {"username": "hogwarts", "password": "test12345"}
    url = "https://litemall.hogwarts.ceshiren.com/admin/auth/login"
    r = requests.post(url, headers=headers, json=login_data)
    global token
    token = r.json().get("data", {}).get("token")
    assert r.status_code==200

@pytest.mark.repeat(1000) # 重复执行该用例10次
def test_Get_goods():
    url = "https://litemall.hogwarts.ceshiren.com/wx/goods/list"
    params = {"keyword": "3D", "page": 1, "limit": 10}
    data = {"X-Litemall-Token": token}
    r = requests.get(url, params=params, data=data)
    assert r.status_code == 200
