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
from selenium import webdriver

def test_ui():
    browser = webdriver.Chrome()
    browser.delete_all_cookies()
    browser.implicitly_wait(10)
    browser.get("https://www.google.ru/")
    browser.maximize_window()
    time.sleep(5)



