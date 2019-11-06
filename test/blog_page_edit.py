from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

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

blog_posts = wait.until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[3]/div[1]/ul/li[1]/ul/li[2]/a')))
blog_posts.click()
title = "heroku"
open_blog = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, title)))
open_blog.click()
title = "heroku"
content = "how to use heroku"
blog_title = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="id_title"]')))
blog_title.clear()
blog_title.send_keys(title)
iframe = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="id_content_ifr"]')))
driver.switch_to.frame(iframe)
blog_content = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/p')))
script = "arguments[0].insertAdjacentHTML('afterEnd', arguments[1])"
driver.execute_script(script, blog_content, content)
driver.switch_to.default_content()
blog_save = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[4]/div/form/div/div/input[1]')))
blog_save.click()
bodyText = wait.until(EC.element_to_be_clickable((By.TAG_NAME, 'body')))
assert "successfully" in bodyText.text

pages = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[3]/div[1]/ul/li[1]/ul/li[1]/a')))
pages.click()
title = "Change Page Status"
open_page = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, title)))
open_page.click()
title = "Change Page Status"
content = "how to use heroku"
page_title = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="id_title"]')))
page_title.clear()
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

driver.quit()