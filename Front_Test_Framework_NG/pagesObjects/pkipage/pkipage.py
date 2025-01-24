from selenium.webdriver.common.by import By
from ...helpers.helpers import HelperFunc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from ...helpers.helpers import HelperFunc





class PkiPage:
    def __init__(self,driver) -> None:
        self.driver = driver
        HelperFunc.clean("locators/pki/pki_page.json")

        
        
    
    def click_dropdown_side_pkis(self):
        aria_expanded_value = self.driver.find_element(By.XPATH,HelperFunc.load("locators/dashbord/dashbrod_page.json").get("administrationDropdown")).get_attribute("aria-expanded")
        if aria_expanded_value == "false":
            HelperFunc.save_results("Test 4 pki : dropdown administration click status")
            self.driver.find_element(By.XPATH,HelperFunc.load("locators/dashbord/dashbrod_page.json").get("administrationDropdown")).click()
            self.driver.implicitly_wait(2)
            time.sleep(2)
            self.driver.find_element(By.XPATH,HelperFunc.load("locators/dashbord/dashbrod_page.json").get("pkis")).click()
            HelperFunc.save_results("Test 4 pki : dropdown pkis click status")
        else:
            self.driver.find_element(By.XPATH,HelperFunc.load("locators/dashbord/dashbrod_page.json").get("pkis")).click()
            HelperFunc.save_results("Test 4 pki : dropdown pkis click status")

        WebDriverWait(self.driver, 60).until(EC.url_changes(self.driver.current_url))
        WebDriverWait(self.driver, 180).until(EC.invisibility_of_element_located((By.ID, "loading")))
        HelperFunc.save_results("Test 4 pki : acess pkis page status")

    def click_add_pki(self):
        if "/#/pki/list" in self.driver.current_url:
            HelperFunc.extract_xpaths(self.driver,"locators/pki/pki_page.json")
            HelperFunc.save_results("Test 4 pki : extract xpaths status")
            self.driver.find_element(By.XPATH,HelperFunc.load("locators/pki/pki_page.json").get("createPki")).click()
            HelperFunc.save_results("Test 4 pki : add pki button click status")
            WebDriverWait(self.driver, 60).until(EC.url_changes(self.driver.current_url))
            WebDriverWait(self.driver, 180).until(EC.invisibility_of_element_located((By.ID, "loading")))
            HelperFunc.save_results("Test 4 pki : new pki status")

    def click_sync(self):
        if "/#/pki/list" in self.driver.current_url:
            HelperFunc.extract_xpaths(self.driver,"locators/pki/pki_page.json")
            HelperFunc.save_results("Test 4 pki : extract xpaths for synch status")
            rep=3
            sync=False
            while rep>0:
                keys_with_prefix = HelperFunc.get_pki_tosync(HelperFunc.load("locators/pki/pki_page.json"), "pkiToSync")
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/pki/pki_page.json").get(keys_with_prefix[-1])).click()
                HelperFunc.save_results("Test 4 pki : sync button click status")
                HelperFunc.extract_xpaths(self.driver,"locators/pki/pki_page.json")
                time.sleep(1)
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/pki/pki_page.json").get("synchronize_authorities")).click()
                time.sleep(1)
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/pki/pki_page.json").get("synchronize_profiles")).click()
                time.sleep(1)
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/pki/pki_page.json").get("syncPKI")).click()
                time.sleep(5)
                HelperFunc.save_results("Test 4 pki : sync request status")
                time.sleep(1)
                if(HelperFunc.verfiy_pki_sync_(self.driver)==True):
                    sync=True
                    break
                    
                else:
                    rep-=1
            if sync==True:
                    print("sync : pki is synced")
            else:
                raise ValueError("sync : pki is not synced")

        