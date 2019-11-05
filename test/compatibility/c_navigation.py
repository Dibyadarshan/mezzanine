from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome(executable_path="/home/anmol/PycharmProjects/prg1/geckodriver-v0.24.0-linux64/chromedriver")
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
pages = wait.until(EC.element_to_be_clickable((By.LINK_TEXT,"Pages")))
pages.click()
assert driver.current_url=="http://127.0.0.1:8000/admin/pages/page/"
driver.back()
blogs = wait.until(EC.element_to_be_clickable((By.LINK_TEXT,'Blog posts')))
blogs.click()
assert driver.current_url=="http://127.0.0.1:8000/admin/blog/blogpost/"
driver.back()
comment = wait.until(EC.element_to_be_clickable((By.LINK_TEXT,'Comments')))
comment.click()
assert driver.current_url=="http://127.0.0.1:8000/admin/generic/threadedcomment/"
driver.back()
media = wait.until(EC.element_to_be_clickable((By.LINK_TEXT,'Media Library')))
media.click()
assert driver.current_url=="http://127.0.0.1:8000/admin/media-library/browse/"
driver.back()
changePassword = wait.until(EC.element_to_be_clickable((By.LINK_TEXT,'Change password')))
changePassword.click()
assert driver.current_url=="http://127.0.0.1:8000/admin/password_change/"
driver.back()
viewOnSite = wait.until(EC.element_to_be_clickable((By.LINK_TEXT,'View site')))
viewOnSite.click()
assert driver.current_url=="http://127.0.0.1:8000/"
driver.quit()
