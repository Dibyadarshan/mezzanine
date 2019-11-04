from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Firefox(executable_path="/home/anmol/PycharmProjects/prg1/geckodriver-v0.24.0-linux64/geckodriver")
wait = WebDriverWait(driver, 10)
# driver.implicitly_wait(2)
driver.get("http://127.0.0.1:8000/blog/test-blog-post/")
driver.maximize_window()

comment_name = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#comment > div:nth-child(7) > input:nth-child(2)')))
comment_name.clear()
comment_name.send_keys("Testing Addition of comment2")
comment_email = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#comment > div:nth-child(8) > input:nth-child(2)')))
comment_email.clear()
comment_email.send_keys('demo@demo.com')
comment_body = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#comment > div:nth-child(10) > textarea:nth-child(2)')))
comment_body.clear()
comment_body.send_keys("Added a new comment")
comment_summit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input.btn:nth-child(1)')))
# print(comment_summit)
comment_summit.click()

reply_reply_element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'reply')))
reply_reply_element.click()
reply_num = reply_reply_element.get_attribute('href')
reply_num = reply_num.strip("http://127.0.0.1:8000/blog/test-blog-post/")
# print(reply_num)
reply_name = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, reply_num + ' > div:nth-child(7) > input:nth-child(2)')))
reply_name.clear()
reply_name.send_keys('Tested Reply2')
reply_email = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, reply_num + ' > div:nth-child(8) > input:nth-child(2)')))
reply_email.clear()
reply_email.send_keys('demo@demo.com')
reply_body = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, reply_num + ' > div:nth-child(10) > textarea:nth-child(2)')))
reply_body.clear()
reply_body.send_keys("Added a new reply")
reply_summit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, reply_num + ' > input:nth-child(13)')))
reply_summit.click()
driver.quit()