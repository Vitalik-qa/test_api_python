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
from selenium.webdriver.common.action_chains import ActionChains


def test_ui():
    browser = webdriver.Chrome()
    browser.delete_all_cookies()
    browser.get("https://www.sberbank.ru/ru/person/kibrary")
    time.sleep(5)
    browser.find_element(By.XPATH, "//a[@title = 'Изменить регион']")
    browser.find_element(By.XPATH, "//a[@title = 'Изменить регион']/following ::a[1]")
    browser.find_element(By.XPATH, "//a[@class= 'kitt-header-search' ]")
    driver.find_element_by_tag_name('body').send_keys(Keys.END)
    time.sleep(5)


#тест - проверка наведения курсора мыши на объект
def test_mouse_over_menu():
    with allure.step("Tест - проверка наведения курсора мыши на объект"):
        driver = webdriver.Chrome()
        driver.delete_all_cookies()
        driver.get("https://www.sberbank.ru/ru/person/kibrary")
        time.sleep(5)

        button_cources = driver.find_element(By.XPATH, "//a[@class= 'kitt-header__link']")
        action.move_to_element(button_cources).click().perform()
        time.sleep(5)

        button_offices = driver.find_element(By.XPATH, "//a[@class= 'kitt-header__link kitt-header__oib'  and text() = 'Офисы']")
        ActionChains(driver).move_to_element(button_offices).perform()
        time.sleep(5)

        button_atm = driver.find_element(By.XPATH, "//a[@class= 'kitt-header__link kitt-header__oib'  and text() = 'Банкоматы']")
        ActionChains(driver).move_to_element(button_atm).perform()
        time.sleep(5)

        button_geo = driver.find_element(By.XPATH, "//a[@title = 'Изменить регион']")
        ActionChains(driver).move_to_element(button_geo).perform()
        time.sleep(5)

        button_eng = driver.find_element(By.XPATH, "//a[@title = 'Изменить регион']/following ::a[1]")
        ActionChains(driver).move_to_element(button_eng).perform()
        time.sleep(5)

        button_search = driver.find_element(By.XPATH, "//a[@class= 'kitt-header-search' ]")
        ActionChains(driver).move_to_element(button_search).perform()
        time.sleep(5)
        driver.quit()

# тест проверяет переключения на английский язык
def test_change_language():
    with allure.step("Тест проверяет переключения на английский язык"):
        driver = webdriver.Chrome()
        driver.delete_all_cookies()
        driver.get("https://www.sberbank.ru/ru/person/kibrary")
        time.sleep(5)
        button_eng = driver.find_element(By.XPATH, "//a[@title = 'Изменить регион']/following ::a[1]")
        button_eng.click()
        time.sleep(5)
        driver.quit()

