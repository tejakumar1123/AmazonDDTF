from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from Test_locators.locators import test_locators
from Test_Excel_functions.excel_functions import teja_excel_functions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import pytest
from PIL import Image


class Test_goodreads:

    @pytest.fixture
    def boot(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        excel_file = 'F:\\DDTF\\Test_Data_output\\test_data.xlsx'
        sheet_name = 'Sheet1'
        self.s = teja_excel_functions(excel_file, sheet_name)
        self.rows = self.s.row_count()
        excel_file2 = 'F:\\DDTF\\Test_Data_output\\test_output.xlsx'
        sheet_name2 = 'Sheet1'
        self.s2 = teja_excel_functions(excel_file2, sheet_name2)
        self.rows2 = self.s2.row_count()
        yield
        self.driver.close()
    '''
    def test_login(self, boot):
        self.driver.get(test_locators.url)
        self.driver.maximize_window()
        wait = WebDriverWait(self.driver, 30)
        rno = 2
        username = self.s.read_data(rno, 6)
        password = self.s.read_data(rno, 7)
        wait.until(EC.visibility_of_element_located((By.XPATH, test_locators().Sign_in))).click()
        wait.until(EC.visibility_of_element_located((By.NAME, test_locators().Username))).send_keys(username)
        wait.until(EC.visibility_of_element_located((By.XPATH, test_locators().continue_button))).click()
        wait.until(EC.visibility_of_element_located((By.NAME, test_locators().Password))).send_keys(password)
        wait.until(EC.presence_of_element_located((By.ID, test_locators().Submit_button))).click()
      
        if self.driver.current_url == 'https://www.amazon.in/?ref_=nav_ya_signin':
           self.s.write_data(rno, 9, "TEST PASS")
        else:
           self.s.write_data(rno, 9, "TEST FAIL")
        
        assert self.driver.title == 'Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in'
        print("SUCCESS : Logged in with Username {a} & {b}".format(a = username, b = password))
    
    def test_search(self, boot):
        self.driver.get(test_locators.url)
        self.driver.maximize_window()
        wait = WebDriverWait(self.driver, 30)
        rno = 3
        username = self.s.read_data(rno, 6)
        password = self.s.read_data(rno, 7)
        searchinput = self.s.read_data(rno, 8)
        wait.until(EC.visibility_of_element_located((By.XPATH, test_locators().Sign_in))).click()
        wait.until(EC.visibility_of_element_located((By.NAME, test_locators().Username))).send_keys(username)
        wait.until(EC.visibility_of_element_located((By.XPATH, test_locators().continue_button))).click()
        wait.until(EC.visibility_of_element_located((By.NAME, test_locators().Password))).send_keys(password)
        wait.until(EC.presence_of_element_located((By.ID, test_locators().Submit_button))).click()
        wait.until(EC.visibility_of_element_located((By.ID, test_locators().Search_box))).send_keys(searchinput)
        wait.until(EC.presence_of_element_located((By.XPATH, test_locators().Submit_search_button))).click()

        if self.driver.current_url.__contains__("Smartwatch"):
           self.s.write_data(rno, 9, "TEST PASS")
        else:
           self.s.write_data(rno, 9, "TEST FAIL")
           self.driver.get_screenshot_as_file("F:\DDTF\Screen1.png")
           image = Image.open("Screen1.png")
           image.show()     
        
        assert self.driver.current_url.__contains__("Smartwatch") == True
        print("SUCCESS : Successfully searched for Smartwatch and taken screeenshot")
    
    def test_allmenu(self, boot):
        self.driver.get(test_locators.url)
        self.driver.maximize_window()
        wait = WebDriverWait(self.driver, 30)
        rno = 4
        rno2 = 2
        username = self.s.read_data(rno, 6)
        password = self.s.read_data(rno, 7)
        wait.until(EC.visibility_of_element_located((By.XPATH, test_locators().Sign_in))).click()
        wait.until(EC.visibility_of_element_located((By.NAME, test_locators().Username))).send_keys(username)
        wait.until(EC.visibility_of_element_located((By.XPATH, test_locators().continue_button))).click()
        wait.until(EC.visibility_of_element_located((By.NAME, test_locators().Password))).send_keys(password)
        wait.until(EC.presence_of_element_located((By.ID, test_locators().Submit_button))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, test_locators().All))).click()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        wait.until(EC.visibility_of_element_located((By.XPATH, test_locators().see_all))).click()
        
        links = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="hmenu-content"]/ul[1]')))
        for list_item in links:
         self.s2.write_data(rno2, 2, list_item.text)
         
        if self.driver.find_element(By.XPATH,test_locators().customer_profile).is_displayed() == True:
           self.s.write_data(rno, 9, "TEST PASS")
        else:
           self.s.write_data(rno, 9, "TEST FAIL")
           self.driver.get_screenshot_as_file("F:\DDTF\Screen2.png")
           image = Image.open("Screen2.png")
           image.show()     
        
        assert self.driver.find_element(By.XPATH,test_locators().customer_profile).is_displayed() == True
        print("SUCCESS : Successfully printed all the allmenu items")
      
    def test_buy(self, boot):
        self.driver.get(test_locators.url)
        self.driver.maximize_window()
        wait = WebDriverWait(self.driver, 30)
        rno = 5
        username = self.s.read_data(rno, 6)
        password = self.s.read_data(rno, 7)
        searchinput = self.s.read_data(rno, 8)
        wait.until(EC.visibility_of_element_located((By.XPATH, test_locators().Sign_in))).click()
        wait.until(EC.visibility_of_element_located((By.NAME, test_locators().Username))).send_keys(username)
        wait.until(EC.visibility_of_element_located((By.XPATH, test_locators().continue_button))).click()
        wait.until(EC.visibility_of_element_located((By.NAME, test_locators().Password))).send_keys(password)
        wait.until(EC.presence_of_element_located((By.ID, test_locators().Submit_button))).click()
        wait.until(EC.visibility_of_element_located((By.ID, test_locators().Search_box))).send_keys(searchinput)
        wait.until(EC.presence_of_element_located((By.XPATH, test_locators().Submit_search_button))).click()
        wait.until(EC.presence_of_element_located((By.XPATH, test_locators().samsung_check_box))).click()
        wait.until(EC.presence_of_element_located((By.XPATH, test_locators().price_50k))).click()
        wait.until(EC.presence_of_element_located((By.XPATH, test_locators().inches))).click()
        wait.until(EC.presence_of_element_located((By.XPATH, test_locators().s_tv))).click()
        wait.until(EC.visibility_of_element_located((By.ID, test_locators().buy))).click()
        wait.until(EC.presence_of_element_located((By.XPATH, test_locators().close_side_window))).click()
        wait.until(EC.presence_of_element_located((By.ID, test_locators().cart))).click()
        wait.until(EC.presence_of_element_located((By.XPATH, test_locators().proceed_to_buy))).click()
        
        if self.driver.current_url.__contains__("addressselect"):
           self.s.write_data(rno, 9, "TEST PASS")
        else:
           self.s.write_data(rno, 9, "TEST FAIL")
           self.driver.get_screenshot_as_file("F:\DDTF\Screen3.png")
           image = Image.open("Screen3.png")
           image.show()     
        
        assert self.driver.current_url.__contains__("addressselect") == True
        print("SUCCESS : Successfully proceeded to buy item page")
      '''
    def test_buy(self, boot):
        self.driver.get(test_locators.url)
        self.driver.maximize_window()
        wait = WebDriverWait(self.driver, 30)
        rno = 6
        rno2 = 3
        username = self.s.read_data(rno, 6)
        password = self.s.read_data(rno, 7)
        searchinput = self.s.read_data(rno, 8)
        wait.until(EC.visibility_of_element_located((By.XPATH, test_locators().Sign_in))).click()
        wait.until(EC.visibility_of_element_located((By.NAME, test_locators().Username))).send_keys(username)
        wait.until(EC.visibility_of_element_located((By.XPATH, test_locators().continue_button))).click()
        wait.until(EC.visibility_of_element_located((By.NAME, test_locators().Password))).send_keys(password)
        wait.until(EC.presence_of_element_located((By.ID, test_locators().Submit_button))).click()
        wait.until(EC.visibility_of_element_located((By.ID, test_locators().Search_box))).send_keys(searchinput)
        wait.until(EC.presence_of_element_located((By.XPATH, test_locators().Submit_search_button))).click()
        
        links = wait.until(EC.presence_of_all_elements_located((By.XPATH, test_locators().search_list)))
        for list_item in links:
         print(list_item.text)
         self.s2.write_data(rno2, 2, list_item.text)

        if self.driver.current_url.__contains__("television"):
           self.s.write_data(rno, 9, "TEST PASS")
        else:
           self.s.write_data(rno, 9, "TEST FAIL")
           self.driver.get_screenshot_as_file("F:\DDTF\Screen4.png")
           image = Image.open("Screen4.png")
           image.show()     
        
        assert self.driver.current_url.__contains__("television") == True
        print("SUCCESS : Successfully listed all items from search result")