import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select


class pageTest(unittest.TestCase):
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

    @unittest.skip("Delete")
    def testDeletepage(self):
        wait = WebDriverWait(self.driver, 10)
        pages = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[3]/div[1]/ul/li[1]/ul/li[1]/a')))
        pages.click()
        title = "Add Page"
        open_page = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, title)))
        open_page.click()
        delete_page = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[4]/div/form/div/div/p/a')))
        delete_page.click()
        confirm_delete = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[4]/form/div/input[2]')))
        confirm_delete.click()
        bodyText = wait.until(EC.element_to_be_clickable((By.TAG_NAME, 'body')))
        self.assertIn("successfully", bodyText.text)

    @unittest.skip("Status")
    def testChangepageStatus(self):
        wait = WebDriverWait(self.driver, 10)
        pages = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[3]/div[1]/ul/li[1]/ul/li[1]/a')))
        pages.click()
        title = "Change Page Status"
        open_page = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, title)))
        open_page.click()
        status_draft = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="id_status_0"]')))
        status_published = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="id_status_1"]')))
        if status_draft.is_selected():
            status_published.click()
        elif status_published.is_selected():
            status_draft.click()
        page_save = wait.until(EC.element_to_be_clickable((By.XPATH, '/ html / body / div[1] / div[4] / div / form / div / div / input[1]')));
        page_save.click()
        bodyText = wait.until(EC.element_to_be_clickable((By.TAG_NAME, 'body')))
        self.assertIn("successfully", bodyText.text)

    @unittest.skip("Modify")
    def testModifypage(self):
        wait = WebDriverWait(self.driver, 10)
        pages = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[3]/div[1]/ul/li[1]/ul/li[1]/a')))
        pages.click()
        title = "Change Page Status"
        open_page = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, title)))
        open_page.click()
        title = "Change Page Status"
        content = "how to use heroku"
        page_title = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="id_title"]')))
        page_title.clear()
        page_title.send_keys(title)
        iframe = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="id_content_ifr"]')))
        self.driver.switch_to.frame(iframe)
        page_content = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/p')))
        script = "arguments[0].insertAdjacentHTML('afterEnd', arguments[1])"
        self.driver.execute_script(script, page_content, content)
        self.driver.switch_to.default_content()
        page_save = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[4]/div/form/div/div/input[1]')))
        page_save.click()
        bodyText = wait.until(EC.element_to_be_clickable((By.TAG_NAME, 'body')))
        self.assertIn("successfully", bodyText.text)

    # @unittest.skip("Publish")
    def testPublishingPage(self):
        wait = WebDriverWait(self.driver, 10)
        pages = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[3]/div[1]/ul/li[1]/ul/li[1]/a')))
        pages.click()
        select_element = wait.until(
            EC.element_to_be_clickable((By.XPATH, '/ html / body / div / div[4] / div / div[1] / select')))
        select_element = Select(select_element);
        select_element.select_by_index(1);
        title = "Add Page"
        content = "learn to Add Page"
        page_title = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="id_title"]')))
        page_title.send_keys(title)
        iframe = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="id_content_ifr"]')))
        self.driver.switch_to.frame(iframe)
        page_content = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/p')))
        script = "arguments[0].insertAdjacentHTML('afterEnd', arguments[1])"
        self.driver.execute_script(script, page_content, content)
        self.driver.switch_to.default_content()
        page_save = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[4]/div/form/div/div/input[1]')))
        page_save.click()
        bodyText = wait.until(EC.element_to_be_clickable((By.TAG_NAME, 'body')))
        self.assertIn("successfully", bodyText.text)

    @unittest.skip("Draft")
    def testSavingpageAsDraft(self):
        wait = WebDriverWait(self.driver, 10)
        pages = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[3]/div[1]/ul/li[1]/ul/li[1]/a')))
        pages.click()
        select_element = wait.until(
            EC.element_to_be_clickable((By.XPATH, '/ html / body / div / div[4] / div / div[1] / select')))
        select_element = Select(select_element);
        select_element.select_by_index(1);
        title = "Add Page As Draft"
        content = "how to Page As Draft"
        page_title = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="id_title"]')))
        page_title.send_keys(title)
        draft = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="id_status_0"]')))
        draft.click()
        iframe = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="id_content_ifr"]')))
        self.driver.switch_to.frame(iframe)
        content_body = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="tinymce"]')))
        page_content = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/p')))
        script = "arguments[0].insertAdjacentHTML('afterEnd', arguments[1])"
        self.driver.execute_script(script, page_content, content)
        self.driver.switch_to.default_content()
        page_save = wait.until(EC.element_to_be_clickable((By.XPATH, '/ html / body / div[1] / div[4] / div / form / div / div / input[1]')))
        page_save.click()
        bodyText = wait.until(EC.element_to_be_clickable((By.TAG_NAME, 'body')))
        self.assertIn("successfully", bodyText.text)

    @classmethod
    def tearDown(self):
        self.driver.close()

if __name__== "__main__":
    unittest.main()