from selenium.webdriver.common.by import By
from ...helpers.helpers import HelperFunc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from ...data.UserData import *



class CreatePage_credentials:
    def __init__(self,driver) -> None:
        self.driver = driver
        if "/#/credential/create" not in driver.current_url:
            raise Exception("You are not on the credentials page")
        HelperFunc.extract_xpaths(driver,"locators/credentials/create_page.json")
        HelperFunc.save_results("Test 3 credentials : extract xpaths status")
    
    def enter_name_credentials(self):
        if "/#/credential/create" in self.driver.current_url:
            self.driver.find_element(By.XPATH,HelperFunc.load("locators/credentials/create_page.json").get("name")).send_keys(credential_name)
            HelperFunc.save_results("Test 3 credentials : enter name status")

    def pick_authnType_Microsoft(self):
        if "/#/credential/create" in self.driver.current_url:
            openORnot = self.driver.find_element(By.XPATH,HelperFunc.load("locators/credentials/create_page.json").get("authnType")).get_attribute("class")
            if "ng-select-opened"  not in  openORnot:
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/credentials/create_page.json").get("authnType")).click()
                time.sleep(2)
                HelperFunc.extract_xpaths(self.driver,"locators/credentials/create_page.json")
                HelperFunc.save_results("Test 3 credentials : extract xpaths for authnType status")
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/credentials/create_page.json").get(str(HelperFunc.search_in_json_file(3,1,"locators/credentials/create_page.json",0)))).click()
                HelperFunc.save_results("Test 3 credentials : pick authnType status")
                time.sleep(2)
                HelperFunc.extract_xpaths(self.driver,"locators/credentials/create_page.json")
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/credentials/create_page.json").get("username")).send_keys(microsft_username)
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/credentials/create_page.json").get("password")).send_keys(microsft_pasword)
                HelperFunc.save_results("Test 3 credentials : data entered status")
            else:
                HelperFunc.extract_xpaths(self.driver,"locators/credentials/create_page.json")
                HelperFunc.save_results("Test 3 credentials : extract xpaths for authnType status")
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/credentials/create_page.json").get(str(HelperFunc.search_in_json_file(3,1,"locators/credentials/create_page.json",0)))).click()
                HelperFunc.save_results("Test 3 credentials : pick authnType status")
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/credentials/create_page.json").get("username")).send_keys(microsft_username)
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/credentials/create_page.json").get("password")).send_keys(microsft_pasword)
                HelperFunc.save_results("Test 3 credentials : data entered status")
            
    def pick_authnType_tls_plain_text(self):
        if "/#/credential/create" in self.driver.current_url:
            openORnot = self.driver.find_element(By.XPATH,HelperFunc.load("locators/credentials/create_page.json").get("authnType")).get_attribute("class")
            if "ng-select-opened"  not in  openORnot:
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/credentials/create_page.json").get("authnType")).click()
                time.sleep(2)
                HelperFunc.extract_xpaths(self.driver,"locators/credentials/create_page.json")
                HelperFunc.save_results("Test 3 credentials : extract xpaths for authnType status")
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/credentials/create_page.json").get(str(HelperFunc.search_in_json_file(4,1,"locators/credentials/create_page.json",0)))).click()
                HelperFunc.save_results("Test 3 credentials : pick authnType status")
                time.sleep(2)
                HelperFunc.extract_xpaths(self.driver,"locators/credentials/create_page.json")
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/credentials/create_page.json").get("upload-certificate")).send_keys(uploadcertificate)
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/credentials/create_page.json").get("upload-PrivateKey")).send_keys(uploadPrivateKey)
                HelperFunc.save_results("Test 3 credentials : data entered status")
            else:
                HelperFunc.extract_xpaths(self.driver,"locators/credentials/create_page.json")
                HelperFunc.save_results("Test 3 credentials : extract xpaths for authnType status")
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/credentials/create_page.json").get(str(HelperFunc.search_in_json_file(4,1,"locators/credentials/create_page.json",0)))).click()
                HelperFunc.save_results("Test 3 credentials : pick authnType status")
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/credentials/create_page.json").get("upload-certificate")).send_keys(uploadcertificate)
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/credentials/create_page.json").get("upload-PrivateKey")).send_keys(uploadPrivateKey)
                HelperFunc.save_results("Test 3 credentials : data entered status")


    def pick_authnType_apache97(self):
        if "/#/credential/create" in self.driver.current_url:
            openORnot = self.driver.find_element(By.XPATH,HelperFunc.load("locators/credentials/create_page.json").get("authnType")).get_attribute("class")
            if "ng-select-opened"  not in  openORnot:
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/credentials/create_page.json").get("authnType")).click()
                time.sleep(2)
                HelperFunc.extract_xpaths(self.driver,"locators/credentials/create_page.json")
                HelperFunc.save_results("Test 3 credentials : extract xpaths for authnType status")
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/credentials/create_page.json").get(str(HelperFunc.search_in_json_file(0,1,"locators/credentials/create_page.json",0)))).click()
                HelperFunc.save_results("Test 3 credentials : pick authnType status")
                time.sleep(2)
                HelperFunc.extract_xpaths(self.driver,"locators/credentials/create_page.json")
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/credentials/create_page.json").get("username")).send_keys(server_username)
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/credentials/create_page.json").get("password")).send_keys(server_password)
                HelperFunc.save_results("Test 3 credentials : data entered status")
            else:
                HelperFunc.extract_xpaths(self.driver,"locators/credentials/create_page.json")
                HelperFunc.save_results("Test 3 credentials : extract xpaths for authnType status")
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/credentials/create_page.json").get(str(HelperFunc.search_in_json_file(0,1,"locators/credentials/create_page.json",0)))).click()
                HelperFunc.save_results("Test 3 credentials : pick authnType status")
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/credentials/create_page.json").get("username")).send_keys(server_username)
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/credentials/create_page.json").get("password")).send_keys(server_password)
                HelperFunc.save_results("Test 3 credentials : data entered status")

    def click_submit_credentials(self):
        self.driver.find_element(By.XPATH,HelperFunc.load("locators/credentials/create_page.json").get("submit")).click()
        WebDriverWait(self.driver, 60).until(EC.url_changes(self.driver.current_url))
        HelperFunc.save_results("Test 3 credentials : submit button click status")
        WebDriverWait(self.driver, 180).until(EC.invisibility_of_element_located((By.ID, "loading")))
        HelperFunc.save_results("Test 3 credentials : new credentials create status")