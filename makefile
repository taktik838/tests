check_left_bt:
	pytest --alluredir src/reports --driver Chrome --driver-path ./chromedriver src/tests/check_left_bt.py
	allure serve src/reports