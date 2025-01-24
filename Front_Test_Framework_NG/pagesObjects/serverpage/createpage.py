from selenium.webdriver.common.by import By
from ...helpers.helpers import HelperFunc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from ...data.UserData import *



class CreatePage_server:
    def __init__(self,driver) -> None:
        self.driver = driver
        if "/#/server/create" not in driver.current_url:
            raise Exception("You are not on the pki page")
        HelperFunc.clean("locators/server/create_page.json")
        HelperFunc.extract_xpaths(driver,"locators/server/create_page.json")
        HelperFunc.save_results("Test 4 server : extract xpaths status")
    
    def enter_name_server(self):
        if "/#/server/create" in self.driver.current_url:
            self.driver.find_element(By.XPATH,HelperFunc.load("locators/server/create_page.json").get("name")).send_keys(apache97_name)
            HelperFunc.save_results("Test 4 server : enter name status")

    def enter_data_ssh(self):
        if "/#/server/create" in self.driver.current_url:
            self.driver.find_element(By.XPATH,HelperFunc.load("locators/server/create_page.json").get("fqdn")).send_keys(apache97_fqdn)
            HelperFunc.save_results("Test 4 server : server fqdn status")
            time.sleep(2)
            self.driver.find_element(By.XPATH,HelperFunc.load("locators/server/create_page.json").get("port")).send_keys(apache97_port)
            HelperFunc.save_results("Test 4 server : server port status")
            time.sleep(2)

    def pick_credentials(self):
        if "/#/server/create" in self.driver.current_url:
            openORnot = self.driver.find_element(By.XPATH,HelperFunc.load("locators/server/create_page.json").get("credential")).get_attribute("class")
            if "ng-select-opened"  not in  openORnot:
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/server/create_page.json").get("credential")).click()
                time.sleep(2)
                HelperFunc.extract_xpaths(self.driver,"locators/server/create_page.json")
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/server/create_page.json").get(str(HelperFunc.search_in_json_file(0,2,"locators/server/create_page.json",-1)))).click()
                HelperFunc.save_results("Test 4 server : pick credentials status")
            else:
                HelperFunc.extract_xpaths(self.driver,"locators/server/create_page.json")
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/server/create_page.json").get(str(HelperFunc.search_in_json_file(0,2,"locators/server/create_page.json",-1)))).click()
                HelperFunc.save_results("Test 4 server : pick credentials status")
    
    def click_submit_server(self):
        self.driver.find_element(By.XPATH,HelperFunc.load("locators/server/create_page.json").get("submit")).click()
        WebDriverWait(self.driver, 60).until(EC.url_changes(self.driver.current_url))
        HelperFunc.save_results("Test 4 server : submit button click status")
        WebDriverWait(self.driver, 180).until(EC.invisibility_of_element_located((By.ID, "loading")))
        HelperFunc.save_results("Test 4 server : new pki create status")

    