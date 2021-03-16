import pytest
import allure
import unittest
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

START_URL = "https://stackoverflow.com/search?q=something"

    
@allure.step("Launch site")
def test_launch_site(driver):
    wait = WebDriverWait(driver, 5)
    
    driver.get(START_URL)
    try:
        wait.until(EC.title_is("Posts containing 'something' - Stack Overflow"))
    except TimeoutException:
        assert driver.title == "Posts containing 'something' - Stack Overflow"
    

def test_next_results(driver: webdriver.Chrome):
    test_launch_site(driver)
    result_ids = list(map(
        lambda x: x.get_attribute('id'), 
        driver.find_elements_by_css_selector('#mainbar > div.flush-left.js-search-results > div > div')
    ))
    with allure.step('Click to Next'):
        bt = driver.find_element_by_css_selector('#mainbar > div.s-pagination.pager.fl > a:nth-child(8)')
        bt.click()
        next_result_ids = list(map(
            lambda x: x.get_attribute('id'), 
            driver.find_elements_by_css_selector('#mainbar > div.flush-left.js-search-results > div > div')
        ))
    assert set(result_ids) & set(next_result_ids) == set(), 'Запросы повторяются'


def test_15_per_page(driver: webdriver.Chrome):
    test_launch_site(driver)
    with allure.step('Click to Next'):
        bt = driver.find_element_by_css_selector('#mainbar > div.s-pagination.page-sizer.fr > a:nth-child(1)')
        bt.click()
        result_ids = list(map(
            lambda x: x.get_attribute('id'), 
            driver.find_elements_by_css_selector('#mainbar > div.flush-left.js-search-results > div > div')
        ))
    assert len(result_ids) == 15

def test_30_per_page(driver: webdriver.Chrome):
    test_launch_site(driver)
    with allure.step('Click to Next'):
        bt = driver.find_element_by_css_selector('#mainbar > div.s-pagination.page-sizer.fr > a:nth-child(2)')
        bt.click()
        result_ids = list(map(
            lambda x: x.get_attribute('id'), 
            driver.find_elements_by_css_selector('#mainbar > div.flush-left.js-search-results > div > div')
        ))
    assert len(result_ids) == 30

def test_50_per_page(driver: webdriver.Chrome):
    test_launch_site(driver)
    with allure.step('Click to Next'):
        bt = driver.find_element_by_css_selector('#mainbar > div.s-pagination.page-sizer.fr > a:nth-child(3)')
        bt.click()
        result_ids = list(map(
            lambda x: x.get_attribute('id'), 
            driver.find_elements_by_css_selector('#mainbar > div.flush-left.js-search-results > div > div')
        ))
    assert len(result_ids) == 50
    
