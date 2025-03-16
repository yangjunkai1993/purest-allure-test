import pytest
import os

pytest.main()

os.system('allure generate -o allure_reports -c temps')  # 生成Allure报告
#os.system('allure open allure_reports')  # 自动打开浏览器展示报告
