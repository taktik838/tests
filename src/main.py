import unittest

from src.tests import check_left_bt

def test_buttons(self):
        driver = webdriver.Chrome('/home/bk-trainee/projects/pytest_allure/chromedriver')
        wait = WebDriverWait(driver, 5)
        
        self.driver = driver
        self.wait = wait
        self.start_url = "https://stackoverflow.com/questions"
        
        self.launch_site()
        self.click_button(
            '#left-sidebar > div.left-sidebar--sticky-container.js-sticky-leftnav > nav > ol > li:nth-child(1) > a',
            next_url='https://stackoverflow.com/',
            bt_name='Home'
        )
        self.come_back()
        self.click_button(
            '#nav-questions',
            next_url='https://stackoverflow.com/questions',
            bt_name='nav-questions'
        )
        self.click_button(
            '#nav-tags',
            next_url='https://stackoverflow.com/tags',
            bt_name='nav-tags'
        )
        self.come_back()
        self.click_button(
            '#nav-users',
            next_url='https://stackoverflow.com/users',
            bt_name='nav-users'
        )
        self.come_back()
        self.click_button(
            '#nav-jobs',
            next_url='https://stackoverflow.com/jobs',
            bt_name='nav-jobs'
        )
        self.come_back()
        self.click_button(
            '#nav-companies',
            next_url='https://stackoverflow.com/jobs/companies',
            bt_name='nav-companies'
        )
        self.come_back()
        self.click_button(
            '#left-sidebar > div.left-sidebar--sticky-container.js-sticky-leftnav > nav > ol > li:nth-child(3) > ol > li.ps-relative.js-create-team-cta > a',
            next_url='https://stackoverflow.com/teams/create',
            bt_name='Create a Team'
        )
    
tests = unittest.TestSuite()
tests.addTest(test)
