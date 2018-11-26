from Behave_Python.framework.webapp import webapp
from selenium.webdriver.common.keys import Keys
import pandas as pd
import xlrd
import time
from page_objects import PageObject, PageElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

delay_min = 3 # sec
delay_medium = 5 # sec
delay_max = 9 # sec


class Dashboard():
    instance = None
    global wb
    global excel_path
    wb = xlrd.open_workbook("C://Users//asingh//PycharmProjects//Selenium_BDD//Behave_Python//Practice//DataExcel.xlsx")
    excel_path = "C://Users//asingh//PycharmProjects//Selenium_BDD//Behave_Python//Practice//DataExcel.xlsx"

    text_box_first_name = PageElement(id_='customer.firstName')
    button_submit_form = PageElement(css="input[value='Register']")
    form_submit_result_message = PageElement(id_='customer.lastName.errors')

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = Dashboard()
        return cls.instance

    def __init__(self):
        self.driver = webapp.get_driver()

    def method_registration_page_clean_database(self, current_web_driver,):
        self.text_box_first_name = 'name_first'
        self.button_submit_form.click()
        WebDriverWait(current_web_driver, delay_medium).\
            until(expected_conditions.visibility_of(self.form_submit_result_message))
        return

    def verify_status(self, row):
        print('Verifying eTouch Home Page status..')
        status = self.driver.find_element_by_xpath('(//a[@class ="dropdown-toggle"])')
        print('Verifying eTouch Home Page Service status.. :' + status.text)
        status.click()
        service = self.driver.find_element_by_xpath('(//ul[@class ="dropdown-menu"])')
        print('\nVerifying eTouch Home Page dashboard status.. :\n\n' + service.text)
        assert row in service.text, "\n Services {} not present in services component\n".format(row)

    def verify_refresh(self):
        # Read the excel (Get the reference of excel)
        links = self.driver.find_elements_by_tag_name("a")
        for link in links:
            print(link.get_attribute("href"))
        status = self.driver.find_element_by_xpath('(//a[@class ="dropdown-toggle"])')
        status.click()
        Keys.PAGE_DOWN
        element = self.driver.\
            find_element_by_xpath("//p[contains(text(),'We help enterprises align technology with business')]")
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        paragraph_1 = element.text
        print("\n Service Page Paragraph 1 :" + paragraph_1)
        df = pd.read_excel(excel_path, sheet_name="Service_WebPage_Paragraph")
        print("Column headings:")
        print('Column count => {0}'.format(len(df.columns)))
        print('Row count => {0}'.format(len(df.index)))
        print('****************************')
        print('Row count 1 => {0}', df.all())
        print('Row count 2 => {2}')
        print('****************************\n')
        print(df['Paragraph_1'][1])
        print(df['Paragraph_2'][1])
        print(df['Paragraph_3'][1])
        print('****************************\n')
        # Loop to get all data
        for i in df.index:
            print(df['Paragraph_1'][i])
            print(df['Paragraph_2'][i])
            print(df['Paragraph_3'][i])
        assert paragraph_1, "On Service Page Paragraph {} not found on page".format(df['Paragraph_2'][1])
        print('Verified Service Page Paragraph assertion..')

    def verify_customer_info(self):
        print(wb.sheet_names())
        sheet = wb.sheet_by_index(0)
        customer = self.driver.find_element_by_xpath(sheet.cell_value(3, 3))
        customer.click()

        customer_page_paragraph_1 = self.driver.find_element_by_xpath(sheet.cell_value(3, 2)).text
        print(sheet.cell_value(3, 1))
        print("Customer Page 1st Paragraph is : {0}   ".format(sheet.cell_value(3, 1)))
        assert customer_page_paragraph_1, "On Customer Page Paragraph {} not found on page".sheet.cell_value(3, 1)
        print('Verified Service Page Paragraph assertion..')


    def verify_battery_refresh(self):
        # Ex:
        # refresh = self.driver.find_element_by_id('dashboard-battery-refresh-btn')
        # refresh.click()
        print('Verifying battery refresh..')

    def verify_gps_setting(self, row):
        # Ex:
        # status = self.driver.find_element_by_id('gps-setting-component').text
        # assert row in status, "{} not present in GPS component".format(row)
        print('Verifying GPS setting..')


dashboard = Dashboard.get_instance()
