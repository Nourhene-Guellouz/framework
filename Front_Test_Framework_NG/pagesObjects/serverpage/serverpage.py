from selenium.webdriver.common.by import By
from ...helpers.helpers import HelperFunc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from ...helpers.helpers import HelperFunc





class ServerPage:
    def __init__(self,driver) -> None:
        self.driver = driver
        HelperFunc.clean("locators/server/server_page.json")

        
        
    
    def click_dropdown_side_servers(self):
        aria_expanded_value = self.driver.find_element(By.XPATH,HelperFunc.load("locators/dashbord/dashbrod_page.json").get("inventoryDropdown")).get_attribute("aria-expanded")
        if aria_expanded_value == "false":
            HelperFunc.save_results("Test 4 server : dropdown inventoryDropdown click status")
            self.driver.find_element(By.XPATH,HelperFunc.load("locators/dashbord/dashbrod_page.json").get("inventoryDropdown")).click()
            self.driver.implicitly_wait(2)
            time.sleep(2)
            self.driver.find_element(By.XPATH,HelperFunc.load("locators/dashbord/dashbrod_page.json").get("hosts")).click()
            HelperFunc.save_results("Test 4 server : dropdown servers click status")
        else:
            self.driver.find_element(By.XPATH,HelperFunc.load("locators/dashbord/dashbrod_page.json").get("hosts")).click()
            HelperFunc.save_results("Test 4 server : dropdown servers click status")

        WebDriverWait(self.driver, 60).until(EC.url_changes(self.driver.current_url))
        WebDriverWait(self.driver, 180).until(EC.invisibility_of_element_located((By.ID, "loading")))
        HelperFunc.save_results("Test 4 server : acess servers page status")

    def click_add_server(self):
        if "/#/server/list" in self.driver.current_url:
            HelperFunc.extract_xpaths(self.driver,"locators/server/server_page.json")
            HelperFunc.save_results("Test 4 server : extract xpaths status")
            self.driver.find_element(By.XPATH,HelperFunc.load("locators/server/server_page.json").get("createHost")).click()
            HelperFunc.save_results("Test 4 server : add server button click status")
            WebDriverWait(self.driver, 60).until(EC.url_changes(self.driver.current_url))
            WebDriverWait(self.driver, 180).until(EC.invisibility_of_element_located((By.ID, "loading")))
            HelperFunc.save_results("Test 4 server : new server status")

    def click_sync(self):
        if "/#/server/list" in self.driver.current_url:
            HelperFunc.extract_xpaths(self.driver,"locators/server/server_page.json")
            HelperFunc.save_results("Test 4 server : extract xpaths for synch status")
            rep=3
            sync=False
            while rep>0:
                keys_with_prefix = HelperFunc.get_pki_tosync(HelperFunc.load("locators/server/server_page.json"), "pkiToSync")
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/server/server_page.json").get(keys_with_prefix[-1])).click()
                HelperFunc.save_results("Test 4 server : sync button click status")
                HelperFunc.extract_xpaths(self.driver,"locators/server/server_page.json")
                time.sleep(1)
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/server/server_page.json").get("synchronize_authorities")).click()
                time.sleep(1)
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/server/server_page.json").get("synchronize_profiles")).click()
                time.sleep(1)
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/server/server_page.json").get("syncPKI")).click()
                time.sleep(5)
                HelperFunc.save_results("Test 4 server : sync request status")
                time.sleep(1)
                if(HelperFunc.verfiy_pki_sync_(self.driver)==True):
                    sync=True
                    break
                    
                else:
                    rep-=1
            if sync==True:
                    print("sync : server is synced")
            else:
                raise ValueError("sync : server is not synced")

        