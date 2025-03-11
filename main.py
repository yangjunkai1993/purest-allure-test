import pytest
import os

pytest.main()

os.system('allure generate -o allure_reports -c temps')