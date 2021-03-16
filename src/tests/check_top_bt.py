import pytest
import allure
import unittest
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

START_URL = "https://stackoverflow.com"

    
@allure.step("Launch site")
def test_launch_site(driver):
    wait = WebDriverWait(driver, 5)
    
    driver.get(START_URL)
    try:
        wait.until(EC.title_is("Stack Overflow - Where Developers Learn, Share, & Build Careers"))
    except TimeoutException:
        assert driver.title == 'Stack Overflow - Where Developers Learn, Share, & Build Careers'
    
def test_bt_menu(driver):
    test_launch_site(driver)
    _click_button(
        driver,
        'body > header > div > div.-main.grid--cell > a.left-sidebar-toggle.p0.ai-center.jc-center.js-left-sidebar-toggle',
        next_url='https://stackoverflow.com/',
        bt_name='menu'
    )
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((
        By.CSS_SELECTOR, 
        '#left-sidebar'
    )))
def test_bt_StackOverflow(driver):
    test_launch_site(driver)
    _click_button(
        driver,
        'body > header > div > div.-main.grid--cell > a.-logo.js-gps-track',
        next_url='https://stackoverflow.com/',
        bt_name='StackOverflow'
    )
def test_bt_About(driver):
    test_launch_site(driver)
    _click_button(
        driver,
        'body > header > div > ol.list-reset.grid.gs4 > li:nth-child(1) > a',
        next_url='https://stackoverflow.com/company',
        bt_name='About'
    )
def test_bt_Products(driver):
    test_launch_site(driver)
    _click_button(
        driver,
        'body > header > div > ol.list-reset.grid.gs4 > li:nth-child(2) > a',
        next_url='https://stackoverflow.com/',
        bt_name='Products'
    )
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((
        By.CSS_SELECTOR, 
        '#products-popover'
    )))
def test_bt_For_teams(driver):
    test_launch_site(driver)
    _click_button(
        driver,
        'body > header > div > ol.list-reset.grid.gs4 > li:nth-child(3) > a',
        next_url='https://stackoverflow.com/teams',
        bt_name='For teams'
    )

    
# @unittest.expectedFailure
def _click_button(driver: webdriver.Chrome, css, next_url, bt_name=''):
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
