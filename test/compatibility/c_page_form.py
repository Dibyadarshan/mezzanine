from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path="/home/anmol/PycharmProjects/prg1/geckodriver-v0.24.0-linux64/chromedriver")
wait = WebDriverWait(driver, 10)
driver.implicitly_wait(10)
driver.get("http://127.0.0.1:8000/admin/login/?next=/admin/")
driver.maximize_window()
username = "demo"
password = "demo"
username_element = wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='id_username']")))
username_element.send_keys(username)
password_element = wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='id_password']")))
password_element.send_keys(password)
login = wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div/div[2]/form/div[2]/input')))
login.click()
assert driver.current_url=="http://127.0.0.1:8000/admin/"
time.sleep(2)
pages = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[3]/div[1]/ul/li[1]/ul/li[1]/a')))
pages.click()
select_element = wait.until(
    EC.element_to_be_clickable((By.XPATH, '/ html / body / div / div[4] / div / div[1] / select')))
select_element = Select(select_element);
select_element.select_by_index(2);
title = "form page"
content = "page form"
page_title = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="id_title"]')))
page_title.send_keys(title)
iframe = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="id_content_ifr"]')))
driver.switch_to.frame(iframe)
page_content = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/p')))
script = "arguments[0].insertAdjacentHTML('afterEnd', arguments[1])"
driver.execute_script(script, page_content, content)
driver.switch_to.default_content()
field = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="id_fields-0-label"]')))
field.send_keys("Field")
ff = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'submit-row')))
driver.execute_script("arguments[0].style.visibility='hidden'", ff)
fieldValue = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="id_fields-0-field_type"]')))
fieldValue = Select(fieldValue)
fieldValue.select_by_visible_text("Single line text")
driver.execute_script("arguments[0].style.visibility='visible'", ff)
page_save = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[4]/div/form/div/div[3]/input[1]')))
page_save.click()
bodyText = wait.until(EC.element_to_be_clickable((By.TAG_NAME, 'body')))
assert "successfully" in bodyText.text

open_page = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, title)))
open_page.click()
view_site = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[4]/div/ul/li[3]/a')))
view_site.click()
# print(driver.window_handles)
time.sleep(2)
window_before = driver.window_handles[0]
window_after = driver.window_handles[1]
driver.switch_to.window(window_after)
# fieldValue = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#id_field_9')))
# fieldValue.send_keys("some value")
# time.sleep(5)
driver.switch_to.window(window_before)
log_out = wait.until(EC.element_to_be_clickable((By.LINK_TEXT,"Log out")))
log_out.click()
bodyText = wait.until(EC.element_to_be_clickable((By.TAG_NAME, 'body')))
assert "Logged out" in bodyText.text
driver.quit()