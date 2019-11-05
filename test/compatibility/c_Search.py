import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path="/home/anmol/PycharmProjects/prg1/geckodriver-v0.24.0-linux64/chromedriver")
wait = WebDriverWait(driver, 10)
# driver.implicitly_wait(2)
driver.get("http://127.0.0.1:8000/blog/test-blog-post/")
driver.maximize_window()
wait = WebDriverWait(driver, 10)
search_element = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[2]/form/div[1]/input')))
search_filter =  wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'select.form-control')))
select_element = Select(search_filter);
select_element.select_by_index(1);
search_key = "heroku"
search_element.clear()
search_element.send_keys(search_key)
search_element = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[2]/form/input')))
search_element.click()
bodyText = wait.until(EC.element_to_be_clickable((By.TAG_NAME, 'body')))
assert search_key in bodyText.text
time.sleep(2)
wait = WebDriverWait(driver, 10)
search_element = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[2]/form/div[1]/input')))
search_key = "pneumonoultramicroscopicsilicovolcanoconiosis"
search_filter =  wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'select.form-control')))
select_element = Select(search_filter);
select_element.select_by_index(0);
search_element.clear()
search_element.send_keys(search_key)
search_element = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[2]/form/input')))
search_element.click()
bodyText = wait.until(EC.element_to_be_clickable((By.TAG_NAME, 'body')))
assert 'No results' in bodyText.text
search_element = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[2]/form/div[1]/input')))
search_filter =  wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'select.form-control')))
select_element = Select(search_filter);
select_element.select_by_index(2);
search_key = "heroku"
search_element.clear()
search_element.send_keys(search_key)
search_element = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[2]/form/input')))
search_element.click()
bodyText = wait.until(EC.element_to_be_clickable((By.TAG_NAME, 'body')))
assert search_key in bodyText.text
driver.quit()



