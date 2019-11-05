import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class loginTest(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="/home/dibyadarshan/Desktop/Github Repos/mezzanine/test/chromedriver")
        self.driver.get("http://127.0.0.1:8000/admin/login/?next=/admin/")
        self.driver.maximize_window()

    def testValidLogin(self):
        driver = self.driver
        username = "demo"
        password = "demo"
        username_element = driver.find_element_by_xpath("//*[@id='id_username']")
        username_element.send_keys(username)
        password_element = driver.find_element_by_xpath("//*[@id='id_password']")
        password_element.send_keys(password)
        password_element.send_keys(Keys.RETURN)
        time.sleep(2)
        self.assertEqual(driver.current_url , "http://127.0.0.1:8000/admin/")

    def testInvalidLogin(self):
        driver = self.driver
        username = "demo"
        password = "demo1"
        username_element = driver.find_element_by_xpath("//*[@id='id_username']")
        username_element.send_keys(username)
        password_element = driver.find_element_by_xpath("//*[@id='id_password']")
        password_element.send_keys(password)
        password_element.send_keys(Keys.RETURN)
        time.sleep(2)
        self.assertNotEqual(driver.current_url , "http://127.0.0.1:8000/admin/")

    def testChangePassword(self):
        driver = self.driver
        username = "demo"
        password = "demo"
        username_element = driver.find_element_by_xpath("//*[@id='id_username']")
        username_element.send_keys(username)
        password_element = driver.find_element_by_xpath("//*[@id='id_password']")
        password_element.send_keys(password)
        password_element.send_keys(Keys.RETURN)
        time.sleep(2)
        self.assertEqual(driver.current_url, "http://127.0.0.1:8000/admin/")
        driver.implicitly_wait(2)
        change_password = driver.find_element_by_xpath('/html/body/div/div[1]/ul/li[2]/a')
        change_password.click()
        old_password_element = driver.find_element_by_xpath('//*[@id="id_old_password"]')
        new_password_element = driver.find_element_by_xpath('//*[@id="id_new_password1"]')
        confirm_password_element = driver.find_element_by_xpath('//*[@id="id_new_password2"]')
        new_password = "demo"
        old_password_element.send_keys(password)
        new_password_element.send_keys(new_password)
        confirm_password_element.send_keys(new_password)
        change_password = driver.find_element_by_xpath('/html/body/div/div[4]/form/div[2]/input')
        change_password.click()
        # time.sleep(2)
        self.assertEqual(driver.current_url, "http://127.0.0.1:8000/admin/password_change/done/")

    @classmethod
    def tearDown(self):
        self.driver.close()

if __name__== "__main__":
    unittest.main()