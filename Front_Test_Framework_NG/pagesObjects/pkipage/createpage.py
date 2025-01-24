from selenium.webdriver.common.by import By
from ...helpers.helpers import HelperFunc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from ...data.UserData import *



class CreatePage_pki:
    def __init__(self,driver) -> None:
        self.driver = driver
        if "/#/pki/create" not in driver.current_url:
            raise Exception("You are not on the pki page")
        HelperFunc.clean("locators/pki/create_page.json")
        HelperFunc.extract_xpaths(driver,"locators/pki/create_page.json")
        HelperFunc.save_results("Test 4 pki : extract xpaths status")
    
    def enter_name_pki(self):
        if "/#/pki/create" in self.driver.current_url:
            self.driver.find_element(By.XPATH,HelperFunc.load("locators/pki/create_page.json").get("name")).send_keys(pki_name)
            HelperFunc.save_results("Test 4 pki : enter name status")

    def pick_authnType_Microsoft(self):
        if "/#/pki/create" in self.driver.current_url:
            openORnot = self.driver.find_element(By.XPATH,HelperFunc.load("locators/pki/create_page.json").get("type")).get_attribute("class")
            if "ng-select-opened"  not in  openORnot:
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/pki/create_page.json").get("type")).click()
                time.sleep(2)
                HelperFunc.extract_xpaths(self.driver,"locators/pki/create_page.json")
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/pki/create_page.json").get(str(HelperFunc.search_in_json_file(2,1,"locators/pki/create_page.json",0)))).click()
                HelperFunc.save_results("Test 4 pki : pick authnType status")
                time.sleep(2)
                HelperFunc.extract_xpaths(self.driver,"locators/pki/create_page.json")
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/pki/create_page.json").get("fqdn")).send_keys(microsft_fqdn)
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/pki/create_page.json").get("port")).send_keys(microsft_port)
                HelperFunc.save_results("Test 4 pki : data entered status")
            else:
                HelperFunc.extract_xpaths(self.driver,"locators/pki/create_page.json")
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/pki/create_page.json").get(str(HelperFunc.search_in_json_file(2,1,"locators/pki/create_page.json",0)))).click()
                HelperFunc.save_results("Test 4 pki : pick authnType status")
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/pki/create_page.json").get("fqdn")).send_keys(microsft_fqdn)
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/pki/create_page.json").get("port")).send_keys(microsft_port)
                HelperFunc.save_results("Test 4 pki : data entered status")

    def pick_authnType_ejbcace(self):
        if "/#/pki/create" in self.driver.current_url:
            openORnot = self.driver.find_element(By.XPATH,HelperFunc.load("locators/pki/create_page.json").get("type")).get_attribute("class")
            if "ng-select-opened"  not in  openORnot:
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/pki/create_page.json").get("type")).click()
                time.sleep(2)
                HelperFunc.extract_xpaths(self.driver,"locators/pki/create_page.json")
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/pki/create_page.json").get(str(HelperFunc.search_in_json_file(1,1,"locators/pki/create_page.json",0)))).click()
                HelperFunc.save_results("Test 4 pki : pick authnType status")
                time.sleep(2)
                HelperFunc.extract_xpaths(self.driver,"locators/pki/create_page.json")
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/pki/create_page.json").get("fqdn")).send_keys(ejbcace_fqdn)
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/pki/create_page.json").get("port")).send_keys(ejbcace_port)
                HelperFunc.save_results("Test 4 pki : data entered status")
            else:
                HelperFunc.extract_xpaths(self.driver,"locators/pki/create_page.json")
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/pki/create_page.json").get(str(HelperFunc.search_in_json_file(1,1,"locators/pki/create_page.json",0)))).click()
                HelperFunc.save_results("Test 4 pki : pick authnType status")
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/pki/create_page.json").get("fqdn")).send_keys(ejbcace_fqdn)
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/pki/create_page.json").get("port")).send_keys(ejbcace_port)
                HelperFunc.save_results("Test 4 pki : data entered status")

    def pick_credentials(self):
        if "/#/pki/create" in self.driver.current_url:
            openORnot = self.driver.find_element(By.XPATH,HelperFunc.load("locators/pki/create_page.json").get("credentials-0")).get_attribute("class")
            if "ng-select-opened"  not in  openORnot:
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/pki/create_page.json").get("credentials-0")).click()
                time.sleep(2)
                HelperFunc.extract_xpaths(self.driver,"locators/pki/create_page.json")
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/pki/create_page.json").get(str(HelperFunc.search_in_json_file(0,2,"locators/pki/create_page.json",-1)))).click()
                HelperFunc.save_results("Test 4 pki : pick credentials status")
            else:
                HelperFunc.extract_xpaths(self.driver,"locators/pki/create_page.json")
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/pki/create_page.json").get(str(HelperFunc.search_in_json_file(0,2,"locators/pki/create_page.json",-1)))).click()
                HelperFunc.save_results("Test 4 pki : pick credentials status")
    
    def click_submit_pki(self):
        self.driver.find_element(By.XPATH,HelperFunc.load("locators/pki/create_page.json").get("submit")).click()
        WebDriverWait(self.driver, 60).until(EC.url_changes(self.driver.current_url))
        HelperFunc.save_results("Test 4 pki : submit button click status")
        WebDriverWait(self.driver, 180).until(EC.invisibility_of_element_located((By.ID, "loading")))
        HelperFunc.save_results("Test 4 pki : new pki create status")

    