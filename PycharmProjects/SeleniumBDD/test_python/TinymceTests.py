import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class TinymceTests(unittest.TestCase):

    def setUp(self):
        # define a driver instance, for example Chrome
        self.driver = webdriver.Chrome('C:\\Users\\asingh\\AppData\\Local\\Programs\\Python\\chromedriver')
        self.driver.maximize_window()

    def test_tinymce_enter_text(self):
        driver = self.driver
        # navigate to the demo website
        driver.get('https://www.tinymce.com/docs/demo/full-featured/')
        time.sleep(2)
        # define Top Frame
        top_frame = driver.find_element_by_id('cp_embed_NGegZK')
        # Switch to the top frame
        driver.switch_to.frame(top_frame)
        # define Result Frame
        result_frame = driver.find_element_by_id('result-iframe')
        # Switch to the result frame
        driver.switch_to.frame(result_frame)
        # define MCE Frame
        mce_frame = driver.find_element_by_id('mce_0_ifr')
        # Switch to the mce frame
        driver.switch_to.frame(mce_frame)
        # define mce body
        mce_edit = driver.find_element_by_xpath("//body[@id='tinymce']")
        time.sleep(5)
        # clear mce body
        mce_edit.clear()
        time.sleep(5)
        mce_edit.send_keys('Selenium Master')
        time.sleep(5)
        mce_edit.send_keys(Keys.ENTER)
        time.sleep(5)
        mce_edit.send_keys('Python Webdriver Tutorial')
        time.sleep(5)
        body_text = mce_edit.text
        # verify that text contains
        self.assertTrue(body_text.find('Python Webdriver Tutorial') > 1)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()

