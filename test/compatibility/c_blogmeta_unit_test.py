import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

class BlogMetaDataTest(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="/home/dibyadarshan/Desktop/Github Repos/mezzanine/test/chromedriver")
        self.driver.get("http://127.0.0.1:8000/admin/login/?next=/admin/")
        self.driver.maximize_window()
        driver = self.driver
        username = "demo"
        password = "demo"
        username_element = driver.find_element_by_xpath("//*[@id='id_username']")
        username_element.send_keys(username)
        password_element = driver.find_element_by_xpath("//*[@id='id_password']")
        password_element.send_keys(password)
        password_element.send_keys(Keys.RETURN)

    def testModifyMetadata(self):
        wait = WebDriverWait(self.driver, 10)
        blog_posts = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[3]/div[1]/ul/li[1]/ul/li[2]/a')))
        blog_posts.click()
        title = "heroku"
        open_blog = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, title)))
        open_blog.click()
        metadata = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[4]/div/form/div/fieldset[3]/h2')))
        self.driver.execute_script("arguments[0].click();", metadata)
        meta_title = "heroku"
        meta_url = "heroku"
        meta_description = "heroku"
        meta_keyword = "heroku"
        blog_meta_title = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="id__meta_title"]')))
        blog_meta_url = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="id_slug"]')))
        blog_meta_description = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="id_description"]')))
        blog_meta_keyword = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="id_keywords_1"]')))
        blog_meta_title.clear()
        blog_meta_url.clear()
        blog_meta_keyword.clear()
        blog_meta_description.clear()
        blog_meta_title.send_keys(meta_title)
        blog_meta_description.send_keys(meta_description)
        blog_meta_keyword.send_keys(meta_keyword)
        blog_meta_url.send_keys(meta_url)
        blog_save = wait.until(EC.element_to_be_clickable((By.XPATH, '/ html / body / div[1] / div[4] / div / form / div / div / input[1]')));
        blog_save.click()
        bodyText = wait.until(EC.element_to_be_clickable((By.TAG_NAME, 'body')))
        self.assertIn("MEZZANINE", bodyText.text)

    def testAddMetaDta(self):
        wait = WebDriverWait(self.driver, 10)
        blog_posts = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[3]/div[1]/ul/li[1]/ul/li[2]/a')))
        blog_posts.click()
        add_blog = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[4]/div/ul/li/a')))
        add_blog.click()
        title = "Github"
        content = "how to use Github"
        blog_title = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="id_title"]')))
        blog_title.send_keys(title)
        iframe = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="id_content_ifr"]')))
        self.driver.switch_to.frame(iframe)
        blog_content = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/p')))
        script = "arguments[0].insertAdjacentHTML('afterEnd', arguments[1])"
        self.driver.execute_script(script, blog_content, content)
        self.driver.switch_to.default_content()
        metadata = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[4]/div/form/div/fieldset[3]/h2')))
        self.driver.execute_script("arguments[0].click();", metadata)
        meta_title = "Github"
        meta_url = "Github"
        meta_description = "github"
        meta_keyword = "github"
        blog_meta_title = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="id__meta_title"]')))
        blog_meta_url = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="id_slug"]')))
        blog_meta_description = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="id_description"]')))
        blog_meta_keyword = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="id_keywords_1"]')))
        blog_meta_title.send_keys(meta_title)
        blog_meta_description.send_keys(meta_description)
        blog_meta_keyword.send_keys(meta_keyword)
        blog_meta_url.send_keys(meta_url)
        blog_save = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[4]/div/form/div/div/input[1]')))
        blog_save.click()
        bodyText = wait.until(EC.element_to_be_clickable((By.TAG_NAME,'body')))
        self.assertIn("successfully", bodyText.text)

    @classmethod
    def tearDown(self):
        self.driver.close()

if __name__== "__main__":
    unittest.main()