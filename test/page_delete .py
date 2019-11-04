from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

driver = webdriver.Firefox(executable_path="/home/anmol/PycharmProjects/prg1/geckodriver-v0.24.0-linux64/geckodriver")
wait = WebDriverWait(driver, 10)
# driver.implicitly_wait(2)
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

pages = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[3]/div[1]/ul/li[1]/ul/li[1]/a')))
pages.click()
select_element = wait.until(
    EC.element_to_be_clickable((By.XPATH, '/ html / body / div / div[4] / div / div[1] / select')))
select_element = Select(select_element);
select_element.select_by_index(1);
title = "Page1 to delete"
content = "how delete a page1"
page_title = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="id_title"]')))
page_title.send_keys(title)
iframe = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="id_content_ifr"]')))
driver.switch_to.frame(iframe)
page_content = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/p')))
script = "arguments[0].insertAdjacentHTML('afterEnd', arguments[1])"
driver.execute_script(script, page_content, content)
driver.switch_to.default_content()
page_save = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[4]/div/form/div/div/input[1]')))
page_save.click()
bodyText = wait.until(EC.element_to_be_clickable((By.TAG_NAME, 'body')))
assert "successfully" in bodyText.text

open_page = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, title)))
open_page.click()
delete_page = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[4]/div/form/div/div/p/a')))
delete_page.click()
confirm_delete = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[4]/form/div/input[2]')))
confirm_delete.click()
bodyText = wait.until(EC.element_to_be_clickable((By.TAG_NAME, 'body')))
assert "successfully" in bodyText.text

pages = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[3]/div[1]/ul/li[1]/ul/li[1]/a')))
pages.click()
select_element = wait.until(
    EC.element_to_be_clickable((By.XPATH, '/ html / body / div / div[4] / div / div[1] / select')))
select_element = Select(select_element);
select_element.select_by_index(1);
title = "Page2 to delete"
content = "how delete a page2"
page_title = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="id_title"]')))
page_title.send_keys(title)
iframe = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="id_content_ifr"]')))
driver.switch_to.frame(iframe)
page_content = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/p')))
script = "arguments[0].insertAdjacentHTML('afterEnd', arguments[1])"
driver.execute_script(script, page_content, content)
driver.switch_to.default_content()
page_save = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[4]/div/form/div/div/input[1]')))
page_save.click()
bodyText = wait.until(EC.element_to_be_clickable((By.TAG_NAME, 'body')))
assert "successfully" in bodyText.text

open_page = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, title)))
open_page.click()
delete_page = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[4]/div/form/div/div/p/a')))
delete_page.click()
confirm_delete = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[4]/form/div/input[2]')))
confirm_delete.click()
bodyText = wait.until(EC.element_to_be_clickable((By.TAG_NAME, 'body')))
assert "successfully" in bodyText.text

pages = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[3]/div[1]/ul/li[1]/ul/li[1]/a')))
pages.click()
select_element = wait.until(
    EC.element_to_be_clickable((By.XPATH, '/ html / body / div / div[4] / div / div[1] / select')))
select_element = Select(select_element);
select_element.select_by_index(1);
title = "Page3 to delete"
content = "how delete a page3"
page_title = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="id_title"]')))
page_title.send_keys(title)
iframe = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="id_content_ifr"]')))
driver.switch_to.frame(iframe)
page_content = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/p')))
script = "arguments[0].insertAdjacentHTML('afterEnd', arguments[1])"
driver.execute_script(script, page_content, content)
driver.switch_to.default_content()
page_save = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[4]/div/form/div/div/input[1]')))
page_save.click()
bodyText = wait.until(EC.element_to_be_clickable((By.TAG_NAME, 'body')))
assert "successfully" in bodyText.text

open_page = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, title)))
open_page.click()
delete_page = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[4]/div/form/div/div/p/a')))
delete_page.click()
confirm_delete = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[4]/form/div/input[2]')))
confirm_delete.click()
bodyText = wait.until(EC.element_to_be_clickable((By.TAG_NAME, 'body')))
assert "successfully" in bodyText.text

log_out = wait.until(EC.element_to_be_clickable((By.LINK_TEXT,"Log out")))
log_out.click()
bodyText = wait.until(EC.element_to_be_clickable((By.TAG_NAME, 'body')))
assert "Logged out" in bodyText.text
driver.quit()