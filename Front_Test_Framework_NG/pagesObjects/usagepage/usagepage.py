from selenium.webdriver.common.by import By
from ...helpers.helpers import HelperFunc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from ...helpers.helpers import HelperFunc





class UsagePage:
    def __init__(self,driver) -> None:
        self.driver = driver
        
        
    
    def click_dropdown_side_usage(self):
        aria_expanded_value = self.driver.find_element(By.XPATH,HelperFunc.load("locators/dashbord/dashbrod_page.json").get("administrationDropdown")).get_attribute("aria-expanded")
        if aria_expanded_value == "false":
            HelperFunc.save_results("Test 6 dashbord : dropdown administration click for usage status")
            self.driver.find_element(By.XPATH,HelperFunc.load("locators/dashbord/dashbrod_page.json").get("administrationDropdown")).click()
            self.driver.implicitly_wait(2)
            time.sleep(2)
            self.driver.find_element(By.XPATH,HelperFunc.load("locators/dashbord/dashbrod_page.json").get("usages")).click()
            HelperFunc.save_results("Test 6 dashbord : dropdown usages click status")

        else:
            self.driver.find_element(By.XPATH,HelperFunc.load("locators/dashbord/dashbrod_page.json").get("usages")).click()
            HelperFunc.save_results("Test 6 dashbord : dropdown usages click status")
        WebDriverWait(self.driver, 60).until(EC.url_changes(self.driver.current_url))
        WebDriverWait(self.driver, 180).until(EC.invisibility_of_element_located((By.ID, "loading")))
        HelperFunc.save_results("Test 6 dashbord : acess usages page status")

    def click_add_usage(self):
        if "/#/usage/list" in self.driver.current_url:
            HelperFunc.extract_xpaths(self.driver,"locators/usage/usage_page.json")
            HelperFunc.save_results("Test 6 usage : extract xpaths status")
            self.driver.find_element(By.XPATH,HelperFunc.load("locators/usage/usage_page.json").get("btn-sm btn btn-primary")).click()
            HelperFunc.save_results("Test 6 usage : add usage button click status")
            WebDriverWait(self.driver, 60).until(EC.url_changes(self.driver.current_url))
            WebDriverWait(self.driver, 180).until(EC.invisibility_of_element_located((By.ID, "loading")))
            HelperFunc.save_results("Test 6 usage : new usage status")
