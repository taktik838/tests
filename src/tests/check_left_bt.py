import pytest
import allure
import unittest
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.story('Your Story here')
@allure.feature('Your Feature here')
class Check_left_buttons(unittest.TestCase):
    
    @allure.step('Come back')
    def come_back(self):
        self.driver.back()
        self.wait.until(EC.url_matches(self.start_url))
        
    @allure.step("Launch site")
    def launch_site(self):
        self.driver.get(self.start_url)
        self.wait.until(EC.title_is("Newest Questions - Stack Overflow"))
        assert self.driver.title == 'Newest Questions - Stack Overflow'
        
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
    
        
    # @unittest.expectedFailure
    def _click_button(self, css, next_url, bt_name=''):
        step_name = 'Verify button'
        if bt_name:
            step_name += f' "{bt_name.strip()}"'
        with allure.step(step_name):
            bt = self.wait.until(EC.visibility_of_element_located((
                By.CSS_SELECTOR, 
                css
            )))
            
        step_name = 'Clicking to button'
        if bt_name:
            step_name += f' "{bt_name.strip()}"'
        with allure.step(step_name):
            bt.click()            
            self.wait.until(EC.url_matches(next_url))
        self.assertEqual(self.driver.current_url, next_url + '123')
