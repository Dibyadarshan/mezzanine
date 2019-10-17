import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class loginTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(executable_path="/home/dibyadarshan/Desktop/Github Repos/mezzanine/test/chromedriver")

    # @unittest.skip("Draft page")
    def test_draft_page(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/admin/login/?next=/admin/")
        username = "demo"
        password = "demo"
        element = driver.find_element_by_xpath("//*[@id='id_username']")
        element.send_keys(username)
        element = driver.find_element_by_xpath("//*[@id='id_password']")
        element.send_keys(password)
        element.send_keys(Keys.RETURN)
        element = driver.find_element_by_xpath('//*[@id="app_content"]/table/tbody/tr[1]/td[1]/a')
        element.click()
        element = driver.find_element_by_xpath('//*[@id="id_status_0"]')
        element.click()
        
        time.sleep(3)

    # @unittest.skip("Page Click Test")'
    def test_page(self):
        driver = self.driver
        print(driver.current_url)

    @classmethod
    def tearDownClass(self):
        self.driver.close()

if __name__== "__main__":
    unittest.main()
