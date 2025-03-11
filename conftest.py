import pytest

@pytest.fixture()
def test_Farmer_big():
    print('我是执行的前置条件')
    yield
    print('我是执行的后置条件')