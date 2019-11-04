import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

class Comment_Sharing_RssTest(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path="/home/anmol/PycharmProjects/prg1/geckodriver-v0.24.0-linux64/geckodriver")
        self.driver.get("http://127.0.0.1:8000/blog/test-blog-post/")
        self.driver.maximize_window()

    def testAddcomment(self):
        wait = WebDriverWait(self.driver, 10)
        comment_name = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#comment > div:nth-child(7) > input:nth-child(2)')))
        comment_name.clear()
        comment_name.send_keys("Testing Addition of comment2")
        comment_email = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#comment > div:nth-child(8) > input:nth-child(2)')))
        comment_email.clear()
        comment_email.send_keys('demo@demo.com')
        comment_body = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#comment > div:nth-child(10) > textarea:nth-child(2)')))
        comment_body.clear()
        comment_body.send_keys("Added a new comment")
        comment_summit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input.btn:nth-child(1)')))
        print(comment_summit)
        comment_summit.click()

    def testReplyToComment(self):
        wait = WebDriverWait(self.driver, 10)
        reply_reply_element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'reply')))
        reply_reply_element.click()
        reply_num = reply_reply_element.get_attribute('href')
        reply_num = reply_num.strip("http://127.0.0.1:8000/blog/test-blog-post/")
        print(reply_num)
        reply_name = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,reply_num+' > div:nth-child(7) > input:nth-child(2)')))
        reply_name.clear()
        reply_name.send_keys('Tested Reply')
        reply_email = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, reply_num +' > div:nth-child(8) > input:nth-child(2)')))
        reply_email.clear()
        reply_email.send_keys('demo@demo.com')
        reply_body = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, reply_num+' > div:nth-child(10) > textarea:nth-child(2)')))
        reply_body.clear()
        reply_body.send_keys("Added a new reply")
        reply_summit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, reply_num+' > input:nth-child(13)')))
        reply_summit.click()

    def testRSS(self):
        wait = WebDriverWait(self.driver, 10)
        driver = self.driver
        rss_element = wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="body"]/div[3]/div/div[3]/div[2]/div/a[1]')))
        rss_element.click()
        self.assertEqual(driver.current_url, "http://127.0.0.1:8000/blog/feeds/rss/")

    def testTwitter(self):
        wait = WebDriverWait(self.driver, 10)
        driver = self.driver
        twitter_element = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Share on Twitter')))
        print(twitter_element)
        twitter_element.click()
        time.sleep(2)
        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)
        self.assertEqual("twitter" in driver.current_url, True)

    def testFacebook(self):
        wait = WebDriverWait(self.driver, 10)
        driver = self.driver
        facebook_element = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Share on Facebook')))
        facebook_element.click()
        time.sleep(2)
        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)
        self.assertEqual("facebook" in driver.current_url, True)


    @classmethod
    def tearDown(self):
        self.driver.quit()

if __name__== "__main__":
    unittest.main()