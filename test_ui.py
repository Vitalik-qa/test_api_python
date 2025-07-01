import pytest
import json
import requests
import allure
import time
import resources.urls as urls
import Steps.support_steps as support_steps
import Steps.generate_json_steps as generate_json_steps
import Steps.assert_steps as assert_steps
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC




def test_ui():
    browser = webdriver.Chrome()
    browser.delete_all_cookies()
    browser.get("https://www.sberbank.ru/ru/person/kibrary")
    time.sleep(5)
    browser.find_element(By.XPATH, "//a[@title = 'Изменить регион']")
    browser.find_element(By.XPATH, "//a[@title = 'Изменить регион']/following ::a[1]")
    browser.find_element(By.XPATH, "//a[@class= 'kitt-header-search' ]")


"""
    search = browser.find_element(By.XPATH, "//div[@subsegment= 'premier']/preceding:: div[1]")
    search.click()

    search_word = browser.find_element(By.NAME, 'text')
    search_word.send_keys("Кредит")

    body = driver.find_element_by_tag_name("body")
    body.click()


    english = browser.find_element(By.XPATH, "//div[text()='English version']")
    english.click()
    time.sleep(5)
"""

