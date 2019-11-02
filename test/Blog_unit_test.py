import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

class BlogTest(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path="/home/anmol/PycharmProjects/prg1/geckodriver-v0.24.0-linux64/geckodriver")
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

    def testDeleteBlog(self):
        wait = WebDriverWait(self.driver, 40)
        blog_posts = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[3]/div[1]/ul/li[1]/ul/li[2]/a')))
        blog_posts.click()
        title = "heroku"
        open_blog = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, title)))
        open_blog.click()
        delete_blog = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[4]/div/form/div/div/p/a')))
        delete_blog.click()
        confirm_delete = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[4]/form/div/input[2]')))
        confirm_delete.click()
        bodyText = wait.until(EC.element_to_be_clickable((By.TAG_NAME, 'body')))
        self.assertIn("successfully", bodyText.text)

    def testChangeBlogStatus(self):
        wait = WebDriverWait(self.driver, 40)
        blog_posts = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[3]/div[1]/ul/li[1]/ul/li[2]/a')))
        blog_posts.click()
        title = "heroku"
        open_blog = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, title)))
        open_blog.click()
        status_draft = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="id_status_0"]')))
        status_published = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="id_status_1"]')))
        if status_draft.is_selected():
            status_published.click()
        elif status_published.is_selected():
            status_draft.click()
        blog_save = wait.until(EC.element_to_be_clickable((By.XPATH, '/ html / body / div[1] / div[4] / div / form / div / div / input[1]')));
        blog_save.click()
        bodyText = wait.until(EC.element_to_be_clickable((By.TAG_NAME, 'body')))
        self.assertIn("successfully", bodyText.text)

    def testModifyBlog(self):
        wait = WebDriverWait(self.driver, 40)
        blog_posts = wait.until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[3]/div[1]/ul/li[1]/ul/li[2]/a')))
        blog_posts.click()
        title = "heroku"
        open_blog = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, title)))
        open_blog.click()
        title = "heroku"
        content = "how to use heroku"
        blog_title = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="id_title"]')))
        blog_title.clear()
        blog_title.send_keys(title)
        iframe = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="id_content_ifr"]')))
        self.driver.switch_to.frame(iframe)
        blog_content = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/p')))
        script = "arguments[0].insertAdjacentHTML('afterEnd', arguments[1])"
        self.driver.execute_script(script, blog_content, content)
        self.driver.switch_to.default_content()
        blog_save = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[4]/div/form/div/div/input[1]')))
        blog_save.click()
        bodyText = wait.until(EC.element_to_be_clickable((By.TAG_NAME, 'body')))
        self.assertIn("successfully", bodyText.text)

    def testPublishingBlog(self):
        wait = WebDriverWait(self.driver, 40)
        blog_posts = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[3]/div[1]/ul/li[1]/ul/li[2]/a')))
        blog_posts.click()
        add_blog = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[4]/div/ul/li/a')))
        add_blog.click()
        title = "heroku"
        content = "how to use heroku"
        blog_title = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="id_title"]')))
        blog_title.send_keys(title)
        iframe = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="id_content_ifr"]')))
        self.driver.switch_to.frame(iframe)
        blog_content = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/p')))
        script = "arguments[0].insertAdjacentHTML('afterEnd', arguments[1])"
        self.driver.execute_script(script, blog_content, content)
        self.driver.switch_to.default_content()
        blog_save = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[4]/div/form/div/div/input[1]')))
        blog_save.click()
        bodyText = wait.until(EC.element_to_be_clickable((By.TAG_NAME, 'body')))
        self.assertIn("successfully", bodyText.text)

    def testSavingBlogAsDraft(self):
        wait = WebDriverWait(self.driver, 40)
        blog_posts = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[3]/div[1]/ul/li[1]/ul/li[2]/a')))
        blog_posts.click()
        add_blog = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[4]/div/ul/li/a')))
        add_blog.click()
        title = "heroku"
        content = "how to use heroku"
        blog_title = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="id_title"]')))
        blog_title.send_keys(title)
        draft = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="id_status_0"]')))
        draft.click()
        iframe = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="id_content_ifr"]')))
        self.driver.switch_to.frame(iframe)
        content_body = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="tinymce"]')))
        blog_content = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/p')))
        script = "arguments[0].insertAdjacentHTML('afterEnd', arguments[1])"
        self.driver.execute_script(script, blog_content, content)
        self.driver.switch_to.default_content()
        blog_save = wait.until(EC.element_to_be_clickable((By.XPATH, '/ html / body / div[1] / div[4] / div / form / div / div / input[1]')))
        blog_save.click()
        bodyText = wait.until(EC.element_to_be_clickable((By.TAG_NAME, 'body')))
        self.assertIn("successfully", bodyText.text)

    @classmethod
    def tearDown(self):
        self.driver.close()

if __name__== "__main__":
    unittest.main()