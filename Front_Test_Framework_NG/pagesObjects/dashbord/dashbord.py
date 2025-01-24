from selenium.webdriver.common.by import By
from ...helpers.helpers import HelperFunc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from ...data.UserData import *



class DashbordPage:
    def __init__(self,driver) -> None:
        self.driver = driver
        if "/#/dashboard" not in driver.current_url:
            raise Exception("You are not on the dashboard page")
        HelperFunc.save_results("Test 2 dashbord : url acess status")
        HelperFunc.clean("locators/dashbord/dashbrod_page.json")
        HelperFunc.extract_xpaths(driver,"locators/dashbord/dashbrod_page.json")
        HelperFunc.save_results("Test 2 dashbord : extract xpaths status")

    def click_dropdown_header(self):
        aria_expanded_value = self.driver.find_element(By.XPATH,HelperFunc.load("locators/dashbord/dashbrod_page.json").get("dropDownToggleMenu")).get_attribute("aria-expanded")
        if aria_expanded_value == "false":
            self.driver.find_element(By.XPATH,HelperFunc.load("locators/dashbord/dashbrod_page.json").get("text-blue mdi mdi-chevron-down")).click()
            self.driver.implicitly_wait(2)
            HelperFunc.save_results("Test 2 dashbord : header dropdown click status")                             
    
    def click_change_tenant(self):
        time.sleep(2)
        aria_expanded_value = self.driver.find_element(By.XPATH,HelperFunc.load("locators/dashbord/dashbrod_page.json").get("organisationChange")).get_attribute("aria-expanded")
        if aria_expanded_value == "false":
            self.driver.find_element(By.XPATH,HelperFunc.load("locators/dashbord/dashbrod_page.json").get("organisationChange")).click()
            self.driver.implicitly_wait(2)
            time.sleep(2)
            HelperFunc.extract_xpaths(self.driver,"locators/dashbord/dashbrod_page.json")
            time.sleep(2)
            self.driver.find_element(By.XPATH,HelperFunc.load("locators/dashbord/dashbrod_page.json").get(tenant_name+"span")).click()
            HelperFunc.save_results("Test 2 dashbord : pick tenant status")
        else:
            self.driver.find_element(By.XPATH,HelperFunc.load("locators/dashbord/dashbrod_page.json").get(tenant_name+"span")).click()
            HelperFunc.save_results("Test 2 dashbord : pick tenant status")
        time.sleep(2)
        WebDriverWait(self.driver, 180).until(EC.invisibility_of_element_located((By.ID, "loading")))
        HelperFunc.save_results("Test 2 dashbord : change tenant status")
    
    def click_create_tenant(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH,HelperFunc.load("locators/dashbord/dashbrod_page.json").get("organisationCreate")).click()
        WebDriverWait(self.driver, 60).until(EC.url_changes(self.driver.current_url))
        WebDriverWait(self.driver, 180).until(EC.invisibility_of_element_located((By.ID, "loading")))
        time.sleep(3)
        HelperFunc.extract_xpaths(self.driver,"locators/dashbord/create_tenant.json")
        self.driver.find_element(By.XPATH,HelperFunc.load("locators/dashbord/create_tenant.json").get("name")).send_keys(tenant_name)
        time.sleep(2)
        self.driver.find_element(By.XPATH,HelperFunc.load("locators/dashbord/create_tenant.json").get("submit")).click()
        time.sleep(60)            
        HelperFunc.save_results("Test 2 dashbord : new tenant create status")
            

    def click_delete_tenant(self):
        time.sleep(2)
        HelperFunc.delete_tenant(self.driver)
        
