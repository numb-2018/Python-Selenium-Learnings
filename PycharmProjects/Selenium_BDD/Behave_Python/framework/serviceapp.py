from selenium import webdriver
from Behave_Python.data.config import settings
from urllib.parse import urljoin


class ServiceApp:
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = ServiceApp()
        return cls.instance


    def get_driver(self):
        return self.driver

    def load_website(self):
        self.driver.get(settings['url2'])

    def goto_page(self, page):
        self.driver.get(urljoin(settings['url2'], page.lower()))

    def verify_component_exists(self, component):
        # Simple implementation
        status = self.driver.find_element_by_xpath('(//a[@href = "index.html"])[2]').text
        print("\nVerifying eTouch Home Page Service status.** HOME *** : " + status)
        assert component in self.driver.find_element_by_xpath('(//ul[@class="nav navbar-nav"])').text, \
            "Component {} not found on page".format(component)
        print("\n**** HEADER CONTENT  *** : " + self.driver.find_element_by_xpath('(//ul[@class="nav navbar-nav"])').text)


serviceapp = ServiceApp.get_instance()



