import pytest
import json
import pytest
import requests
import allure
import time
import resources.urls as urls
import Steps.support_steps as support_steps
import Steps.generate_json_steps as generate_json_steps
import Steps.assert_steps as assert_steps
import resources.locators as locators
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys




@pytest.mark.smoke_tests
@pytest.mark.regress_tests
@pytest.mark.positive_tests
def test_ui_search():
    try:
        with allure.step("Открытие сайта"):
            browser = webdriver.Chrome()
            browser.delete_all_cookies()
            browser.get("https://ya.ru")
            time.sleep(5)
        with allure.step("Поиск по 'Погода'"):
            search = browser.find_element(By.XPATH, locators.SEARCH)
            search.click()
            search.send_keys("Погода")
            search.send_keys(Keys.ENTER)
            time.sleep(5)

    except Exception:
        browser.save_screenshot('error.png')
        raise

    finally:
        browser.quit()


@pytest.mark.smoke_tests
@pytest.mark.regress_tests
@pytest.mark.positive_tests
def test_ui_currency():
    try:
        with allure.step("Открытие сайта"):
            browser = webdriver.Chrome()
            browser.delete_all_cookies()
            browser.get("https://ya.ru")
            time.sleep(5)
        with allure.step("Поиск Валют на страницы"):
            USD = browser.find_element(By.XPATH, locators.USD)
            EUR = browser.find_element(By.XPATH, locators.EUR)
            YDEX = browser.find_element(By.XPATH, locators.YDEX)

    except Exception:
        browser.save_screenshot('error.png')
        raise

    finally:
        browser.quit()