import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class checktest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Firefox(executable_path="/home/anmol/PycharmProjects/prg1/geckodriver-v0.24.0-linux64/geckodriver")

    def test_login(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/admin/login/?next=/admin/")
        usr = "demo"
        pswd = "demo"
        elem1 = driver.find_element_by_xpath("//*[@id='id_username']")
        # elem.clear()
        elem1.send_keys(usr)
        elem = driver.find_element_by_xpath("//*[@id='id_password']")
        # elem.clear()

        elem.send_keys(pswd)
        login_attempt = driver.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/input")
        login_attempt.submit()

        # self.driver.get("http://127.0.0.1:8000/admin/pages/page/")
        driver.implicitly_wait(3)
        pages = driver.find_element_by_link_text("Pages")
        pages.click()


    @unittest.skip("Save Draft")
    def test_save_draft(self):
        def test_login(self):
            driver = self.driver
            driver.get("http://127.0.0.1:8000/admin/login/?next=/admin/")
            usr = "demo"
            pswd = "demo"
            elem1 = driver.find_element_by_xpath("//*[@id='id_username']")
            # elem.clear()
            elem1.send_keys(usr)
            elem = driver.find_element_by_xpath("//*[@id='id_password']")
            # elem.clear()
            elem.send_keys(pswd)
            # round = driver.find_element_by_xpath("//*[@id='interface_site']")
            # round.click()
            login_attempt = driver.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/input")
            login_attempt.submit()
            # self.driver.get("http://127.0.0.1:8000/admin/pages/page/")
            driver.implicitly_wait(3)
            btt = self.driver.find_element_by_xpath("//*[@id='id_content']")
            btt2 = self.driver.find_element_by_xpath("//*[@id='id_title']")
            # print(btt)
            btt.send_keys(pswd)
            btt2.send_keys(usr)
            savedraft = self.driver.find_element_by_xpath(
                "/html/body/div/div[4]/div[1]/div[1]/form/table/tbody/tr[3]/td[2]/input")
            savedraft.submit()
            # elem.send_keys(Keys.RETURN)
            # driver.close()
            # self.assertEqual(1, 0, "Hello")

    @unittest.skip("hs")
    def test_upload(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/admin/media-library/upload/?ot=desc&o=date")
        btt = driver.find_element_by_xpath("/html/body/div/div[4]/div/form/div/fieldset[1]/div/div/label")
        btt.click()


if __name__== "__main__":
    unittest.main()
# driver.close()