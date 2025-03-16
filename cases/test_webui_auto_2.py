import pytest
from time import sleep

@pytest.mark.repeat(5)
def test_Homepage_elements(driver):
    # 打开网页
    driver.get("https://www.leedarson.com/")
    #print("当前页面标题:", driver.title)
    sleep(10)
    assert 'LEEDARSON' in driver.title


