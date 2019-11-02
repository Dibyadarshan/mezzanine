import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

class pageMetaDataTest(unittest.TestCase):
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

    def testModifyMetadata(self):
        wait = WebDriverWait(self.driver, 40)
        pages = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[3]/div[1]/ul/li[1]/ul/li[1]/a')))
        pages.click()
        title = "Modify Meta Data"
        open_page = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, title)))
        open_page.click()
        metadata = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[4]/div/form/div/fieldset[2]/h2')))
        self.driver.execute_script("arguments[0].click();", metadata)
        meta_title = "heroku"
        meta_url = "heroku"
        meta_description = "heroku"
        meta_keyword = "heroku"
        page_meta_title = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="id__meta_title"]')))
        page_meta_url = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="id_slug"]')))
        page_meta_description = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="id_description"]')))
        page_meta_keyword = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="id_keywords_1"]')))
        page_meta_title.clear()
        page_meta_url.clear()
        page_meta_keyword.clear()
        page_meta_description.clear()
        page_meta_title.send_keys(meta_title)
        page_meta_description.send_keys(meta_description)
        page_meta_keyword.send_keys(meta_keyword)
        page_meta_url.send_keys(meta_url)
        page_save = wait.until(EC.element_to_be_clickable((By.XPATH, '/ html / body / div[1] / div[4] / div / form / div / div / input[1]')));
        page_save.click()
        bodyText = wait.until(EC.element_to_be_clickable((By.TAG_NAME, 'body')))
        self.assertIn("successfully", bodyText.text)

    def testAddMetaDta(self):
        wait = WebDriverWait(self.driver, 40)
        pages = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[3]/div[1]/ul/li[1]/ul/li[1]/a')))
        pages.click()
        select_element = wait.until(EC.element_to_be_clickable((By.XPATH, '/ html / body / div / div[4] / div / div[1] / select')))
        select_element = Select(select_element);
        select_element.select_by_index(1);
        title = "Django"
        content = "learn to use Django"
        page_title = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="id_title"]')))
        page_title.send_keys(title)
        iframe = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="id_content_ifr"]')))
        self.driver.switch_to.frame(iframe)
        page_content = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/p')))
        script = "arguments[0].insertAdjacentHTML('afterEnd', arguments[1])"
        self.driver.execute_script(script, page_content, content)
        self.driver.switch_to.default_content()
        metadata = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[4]/div/form/div/fieldset[2]/h2')))
        self.driver.execute_script("arguments[0].click();", metadata)
        meta_title = "Django"
        meta_url = "Django"
        meta_description = "Django"
        meta_keyword = "Django"
        page_meta_title = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="id__meta_title"]')))
        page_meta_url = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="id_slug"]')))
        page_meta_description = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="id_description"]')))
        page_meta_keyword = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="id_keywords_1"]')))
        page_meta_title.send_keys(meta_title)
        page_meta_description.send_keys(meta_description)
        page_meta_keyword.send_keys(meta_keyword)
        page_meta_url.send_keys(meta_url)
        page_save = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[4]/div/form/div/div/input[1]')))
        page_save.click()
        bodyText = wait.until(EC.element_to_be_clickable((By.TAG_NAME,'body')))
        self.assertIn("successfully", bodyText.text)

    @classmethod
    def tearDown(self):
        self.driver.close()

if __name__== "__main__":
    unittest.main()