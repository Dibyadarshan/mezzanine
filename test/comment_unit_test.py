import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

class BlogTest(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="/home/dibyadarshan/Desktop/Github Repos/mezzanine/test/chromedriver")
        self.driver.get('http://127.0.0.1:8000/blog/test-blog-post/')
        self.driver.maximize_window()

    def testRSS(self):
        wait = WebDriverWait(self.driver, 10)
        driver = self.driver
        rss_element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="body"]/div[3]/div/div[3]/div[2]/div/a[1]')))
        rss_element.click()
        self.assertEqual(driver.current_url , "http://127.0.0.1:8000/blog/feeds/rss/")

    def testTwitter(self):
        wait = WebDriverWait(self.driver, 10)
        driver = self.driver
        twitter_element = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Share on Twitter')))
        twitter_element.click()
        window_before = driver.window_handles[0]
        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)
        self.assertEqual("twitter" in driver.current_url, True)

    def testFacebook(self):
        wait = WebDriverWait(self.driver, 10)
        driver = self.driver
        facebook_element = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Share on Facebook')))
        facebook_element.click()
        window_before = driver.window_handles[0]
        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)
        self.assertEqual("facebook" in driver.current_url, True) 

    @classmethod
    def tearDown(self):
        self.driver.quit()

if __name__== "__main__":
    unittest.main()