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

blog_posts = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[3]/div[1]/ul/li[1]/ul/li[2]/a')))
blog_posts.click()
add_blog = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[4]/div/ul/li/a')))
add_blog.click()
title = "Blog1 to delete"
content = "how delete a blog1"
blog_title = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="id_title"]')))
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

open_blog = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, title)))
open_blog.click()
delete_blog = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[4]/div/form/div/div/p/a')))
delete_blog.click()
confirm_delete = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[4]/form/div/input[2]')))
confirm_delete.click()
bodyText = wait.until(EC.element_to_be_clickable((By.TAG_NAME, 'body')))
assert "successfully" in bodyText.text

blog_posts = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[3]/div[1]/ul/li[1]/ul/li[2]/a')))
blog_posts.click()
add_blog = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[4]/div/ul/li/a')))
add_blog.click()
title = "Blog2 to delete"
content = "how delete a blog2"
blog_title = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="id_title"]')))
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

open_blog = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, title)))
open_blog.click()
delete_blog = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[4]/div/form/div/div/p/a')))
delete_blog.click()
confirm_delete = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[4]/form/div/input[2]')))
confirm_delete.click()
bodyText = wait.until(EC.element_to_be_clickable((By.TAG_NAME, 'body')))
assert "successfully" in bodyText.text


blog_posts = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[3]/div[1]/ul/li[1]/ul/li[2]/a')))
blog_posts.click()
add_blog = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[4]/div/ul/li/a')))
add_blog.click()
title = "Blog3 to delete"
content = "how delete a blog3"
blog_title = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="id_title"]')))
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

open_blog = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, title)))
open_blog.click()
delete_blog = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[4]/div/form/div/div/p/a')))
delete_blog.click()
confirm_delete = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[4]/form/div/input[2]')))
confirm_delete.click()
bodyText = wait.until(EC.element_to_be_clickable((By.TAG_NAME, 'body')))
assert "successfully" in bodyText.text

log_out = wait.until(EC.element_to_be_clickable((By.LINK_TEXT,"Log out")))
log_out.click()
bodyText = wait.until(EC.element_to_be_clickable((By.TAG_NAME, 'body')))
assert "Logged out" in bodyText.text
driver.quit()