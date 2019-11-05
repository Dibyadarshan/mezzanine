import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

if __name__== "__main__":
    driver = webdriver.Chrome(executable_path="/home/dibyadarshan/Desktop/Github Repos/mezzanine/test/chromedriver")
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
    media_element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="side-panel"]/div[1]/ul/li[1]/ul/li[4]/a')))
    time.sleep(2)
    media_element.click()
    folder_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="content-main"]/ul/li[1]/a')))
    folder_button.click()
    text_area = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="id_dir_name"]')))
    text_area.send_keys('Testing folder 2')
    text_area.send_keys(Keys.RETURN)


    folder_area = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="changelist"]/div[1]/div/div/table/tbody/tr[1]/td[2]/b/a')))
    folder_area.click()
    upload_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="content-main"]/ul/li[2]/a')))
    upload_button.click()
    driver.find_element_by_name('Filedata').send_keys('/home/dibyadarshan/test1.txt')
    time.sleep(2)
    driver.find_element_by_name('Filedata').send_keys('/home/dibyadarshan/test2.txt')
    time.sleep(2)
    upload = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="upload-form"]/div/div/input')))
    upload.click()

    media_element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/h1/span/a')))
    media_element.click()

    delete_element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="changelist"]/div[1]/div/div/table/tbody/tr[1]/td[6]/a')))
    delete_element.click()

    wait.until(EC.alert_is_present())
    deletion = driver.switch_to.alert
    deletion.accept()

    driver.quit()