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
time.sleep(2)
change_password = wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div/div[1]/ul/li[2]/a')))
change_password.click()
old_password_element = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="id_old_password"]')))
new_password_element = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="id_new_password1"]')))
confirm_password_element = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="id_new_password2"]')))
new_password = "demo2"
old_password_element.send_keys("demo")
new_password_element.send_keys(new_password)
confirm_password_element.send_keys(new_password)
change_password = driver.find_element_by_xpath('/html/body/div/div[4]/form/div[2]/input')
change_password.click()
# time.sleep(2)
assert driver.current_url=="http://127.0.0.1:8000/admin/password_change/done/"
log_out = wait.until(EC.element_to_be_clickable((By.LINK_TEXT,"Log out")))
log_out.click()
bodyText = wait.until(EC.element_to_be_clickable((By.TAG_NAME, 'body')))
assert "Logged out" in bodyText.text
login_again = wait.until(EC.element_to_be_clickable((By.LINK_TEXT,"Log in again")))
login_again.click()
username = "demo"
password = "demo2"
username_element = wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='id_username']")))
username_element.send_keys(username)
password_element = wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='id_password']")))
password_element.send_keys(password)
login = wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div/div[2]/form/div[2]/input')))
login.click()
assert driver.current_url=="http://127.0.0.1:8000/admin/"
change_password = wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div/div[1]/ul/li[2]/a')))
change_password.click()
old_password_element = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="id_old_password"]')))
new_password_element = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="id_new_password1"]')))
confirm_password_element = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="id_new_password2"]')))
new_password = "demo"
old_password_element.send_keys("demo2")
new_password_element.send_keys(new_password)
confirm_password_element.send_keys(new_password)
change_password = driver.find_element_by_xpath('/html/body/div/div[4]/form/div[2]/input')
change_password.click()
# time.sleep(2)
assert driver.current_url=="http://127.0.0.1:8000/admin/password_change/done/"
log_out = wait.until(EC.element_to_be_clickable((By.LINK_TEXT,"Log out")))
log_out.click()
bodyText = wait.until(EC.element_to_be_clickable((By.TAG_NAME, 'body')))
assert "Logged out" in bodyText.text
driver.quit()