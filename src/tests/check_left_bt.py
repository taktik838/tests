import pytest
import allure
import unittest
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

START_URL = "https://stackoverflow.com/questions"

    
@allure.step("Launch site")
def test_launch_site(driver):
    wait = WebDriverWait(driver, 5)
    
    driver.get(START_URL)
    try:
        wait.until(EC.title_is("Newest Questions - Stack Overflow"))
    except TimeoutException:
        assert driver.title == 'Newest Questions - Stack Overflow'
    
def test_bt_Home(driver):
    test_launch_site(driver)
    _click_button(
        driver,
        '#left-sidebar > div.left-sidebar--sticky-container.js-sticky-leftnav > nav > ol > li:nth-child(1) > a',
        next_url='https://stackoverflow.com/',
        bt_name='Home'
    )
def test_bt_nav_questions(driver):
    test_launch_site(driver)
    _click_button(
        driver,
        '#nav-questions',
        next_url='https://stackoverflow.com/questions',
        bt_name='nav-questions'
    )
def test_bt_nav_tags(driver):
    test_launch_site(driver)
    _click_button(
        driver,
        '#nav-tags',
        next_url='https://stackoverflow.com/tags',
        bt_name='nav-tags'
    )
def test_bt_nav_users(driver):
    test_launch_site(driver)
    _click_button(
        driver,
        '#nav-users',
        next_url='https://stackoverflow.com/users',
        bt_name='nav-users'
    )
def test_bt_nav_jobs(driver):
    test_launch_site(driver)
    _click_button(
        driver,
        '#nav-jobs',
        next_url='https://stackoverflow.com/jobs',
        bt_name='nav-jobs'
    )
def test_bt_nav_companies(driver):
    test_launch_site(driver)
    _click_button(
        driver,
        '#nav-companies',
        next_url='https://stackoverflow.com/jobs/companies',
        bt_name='nav-companies'
    )
def test_bt_Create_a_team(driver):
    test_launch_site(driver)
    _click_button(
        driver,
        '#left-sidebar > div.left-sidebar--sticky-container.js-sticky-leftnav > nav > ol > li:nth-child(3) > ol > li.ps-relative.js-create-team-cta > a',
        next_url='https://stackoverflow.com/teams/create',
        bt_name='Create a Team'
    )

    
# @unittest.expectedFailure
def _click_button(driver, css, next_url, bt_name=''):
    wait = WebDriverWait(driver, 5)
    
    step_name = 'Verify button'
    if bt_name:
        step_name += f' "{bt_name.strip()}"'
    with allure.step(step_name):
        bt = wait.until(EC.visibility_of_element_located((
            By.CSS_SELECTOR, 
            css
        )))
        
    step_name = 'Clicking to button'
    if bt_name:
        step_name += f' "{bt_name.strip()}"'
    with allure.step(step_name):
        bt.click()            
        wait.until(EC.url_matches(next_url))
    assert driver.current_url == next_url
