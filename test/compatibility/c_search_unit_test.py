import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

class SearchKeyTest(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="/home/dibyadarshan/Desktop/Github Repos/mezzanine/test/chromedriver")
        self.driver.get("http://127.0.0.1:8000/")
        self.driver.maximize_window()

    def testSearchExistingKey(self):
        wait = WebDriverWait(self.driver, 10)
        search_element = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[2]/form/div[1]/input')))
        search_key = "heroku"
        search_element.send_keys(search_key)
        search_element = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[2]/form/input')))
        search_element.click()
        bodyText = wait.until(EC.element_to_be_clickable((By.TAG_NAME, 'body')))
        self.assertIn(search_key, bodyText.text)

    def testSearchNoExistingKey(self):
        wait = WebDriverWait(self.driver, 10)
        search_element = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[2]/form/div[1]/input')))
        search_key = "pneumonoultramicroscopicsilicovolcanoconiosis"
        search_element.send_keys(search_key)
        search_element = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[2]/form/input')))
        search_element.click()
        bodyText = wait.until(EC.element_to_be_clickable((By.TAG_NAME, 'body')))
        self.assertIn('No results', bodyText.text)

    @classmethod
    def tearDown(self):
        self.driver.close()

if __name__== "__main__":
    unittest.main()