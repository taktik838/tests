check_left_bt:
	- pytest --alluredir src/reports --driver Chrome --driver-path ./chromedriver src/tests/check_left_bt.py
	allure serve src/reports
check_top_bt:
	- pytest --alluredir src/reports --driver Chrome --driver-path ./chromedriver src/tests/check_top_bt.py
	allure serve src/reports
check_sercher:
	- pytest --alluredir src/reports --driver Chrome --driver-path ./chromedriver src/tests/check_sercher.py
	allure serve src/reports
clear_reports:
	rm -f src/reports/*
install_allure:
	sudo apt install npm
	sudo npm install -g allure-commandline —save-dev