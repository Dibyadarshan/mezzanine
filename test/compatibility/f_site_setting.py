import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

if __name__== "__main__":
    driver = webdriver.Firefox(executable_path="/home/dibyadarshan/Desktop/Github Repos/mezzanine/test/geckodriver")
    driver.get("http://127.0.0.1:8000/admin/login/?next=/admin/")
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
        
    username = "demo"
    password = "demo"
    username_element = driver.find_element_by_xpath("//*[@id='id_username']")
    username_element.send_keys(username)
    password_element = driver.find_element_by_xpath("//*[@id='id_password']")
    password_element.send_keys(password)
    password_element.send_keys(Keys.RETURN)
    setting_element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="side-panel"]/div[1]/ul/li[2]/ul/li[3]/a')))
    time.sleep(2)
    setting_element.click()

    element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="id_COMMENTS_ACCOUNT_REQUIRED"]')))
    element.click()
    element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="settings-form"]/div[5]/input')))
    element.click()

    bodyText = wait.until(EC.element_to_be_clickable((By.TAG_NAME, 'body')))
    assert "Settings were successfully updated." in bodyText.text

    driver.quit()
