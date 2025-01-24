from selenium.webdriver.common.by import By
from ...helpers.helpers import HelperFunc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time




class CredentialPage:
    def __init__(self,driver) -> None:
        self.driver = driver
        if "/#/dashboard" not in driver.current_url:
            raise Exception("You are not on the dashboard page")
        HelperFunc.save_results("Test 3 dashbord : url acess after tenant change status")
        
    
    def click_dropdown_side(self):
        if "/#/dashboard" in self.driver.current_url:
            aria_expanded_value = self.driver.find_element(By.XPATH,HelperFunc.load("locators/dashbord/dashbrod_page.json").get("administrationDropdown")).get_attribute("aria-expanded")
            if aria_expanded_value == "false":
                HelperFunc.save_results("Test 3 dashbord : dropdown administration click status")
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/dashbord/dashbrod_page.json").get("administrationDropdown")).click()
                self.driver.implicitly_wait(2)
                time.sleep(2)
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/dashbord/dashbrod_page.json").get("credentials")).click()
                HelperFunc.save_results("Test 3 dashbord : dropdown credentials click status")
            else:
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/dashbord/dashbrod_page.json").get("credentials")).click()
                HelperFunc.save_results("Test 3 dashbord : dropdown credentials click status")
            WebDriverWait(self.driver, 60).until(EC.url_changes(self.driver.current_url))
            WebDriverWait(self.driver, 180).until(EC.invisibility_of_element_located((By.ID, "loading")))
            HelperFunc.save_results("Test 3 dashbord : acess credentials page status")

    def click_add_credential(self):
        if "/#/credential/list" in self.driver.current_url:
            HelperFunc.extract_xpaths(self.driver,"locators/credentials/credentials_page.json")
            HelperFunc.save_results("Test 3 credentials : extract xpaths status")
            self.driver.find_element(By.XPATH,HelperFunc.load("locators/credentials/credentials_page.json").get("createCredentials")).click()
            HelperFunc.save_results("Test 3 credentials : add credential button click status")
            WebDriverWait(self.driver, 60).until(EC.url_changes(self.driver.current_url))
            WebDriverWait(self.driver, 180).until(EC.invisibility_of_element_located((By.ID, "loading")))
            HelperFunc.save_results("Test 3 credentials : new credential status")