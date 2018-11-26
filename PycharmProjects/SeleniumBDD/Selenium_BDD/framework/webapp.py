from selenium import webdriver
from Selenium_BDD.data.config import settings
from urllib.parse import urljoin


class WebApp:
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = WebApp()
        return cls.instance

    def __init__(self):
        if str(settings['browser']).lower() is "firefox":
            self.driver = webdriver.Firefox()
                #(executable_path='C:\\Users\\asingh\\AppData\\Local\\Programs\\Python\\geckodriver')
        elif str(settings['browser']).lower() is "chrome":
            self.driver = webdriver.Chrome()
            #('C:\\Users\\asingh\\AppData\\Local\\Programs\\Python\\chromedriver')
        else:
            self.driver = webdriver.Firefox()
            #(executable_path='C:\\Users\\asingh\\AppData\\Local\\Programs\\Python\\geckodriver')

    def get_driver(self):
        return self.driver

    def load_website(self):
        self.driver.get(settings['url'])

    def goto_page(self, page):
        self.driver.get(urljoin(settings['url'], page.lower()))

    def verify_component_exists(self, component):
        # Simple implementation
        assert component in self.driver.find_element_by_tag_name('body').text, \
            "Component {} not found on page".format(component)


webapp = WebApp.get_instance()
