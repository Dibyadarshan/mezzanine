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

    @classmethod
    def tearDown(self):
        self.driver.close()

if __name__== "__main__":
    unittest.main()