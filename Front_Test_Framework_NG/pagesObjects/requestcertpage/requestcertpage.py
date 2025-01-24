from selenium.webdriver.common.by import By
from ...helpers.helpers import HelperFunc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from ...helpers.helpers import HelperFunc
from selenium.webdriver.common.keys import Keys





class RequestCertPage:
    def __init__(self,driver) -> None:
        self.driver = driver
        HelperFunc.clean("locators/request_cert/requestcert_page.json")

        
    def click_Request_Cert(self):
        self.driver.find_element(By.XPATH,HelperFunc.load("locators/dashbord/dashbrod_page.json").get("newCertificateRequest")).click()
        HelperFunc.save_results("Test 7 RequestCert : Add RequestCertPage clicked status")
        WebDriverWait(self.driver, 60).until(EC.url_changes(self.driver.current_url))
        WebDriverWait(self.driver, 180).until(EC.invisibility_of_element_located((By.ID, "loading")))
        HelperFunc.save_results("Test 7 RequestCert : acces RequestCertPage clicked status")

    def pick_usage(self):
        if "/#/certificate-request/create" in self.driver.current_url:
            HelperFunc.extract_xpaths(self.driver,"locators/request_cert/requestcert_page.json")
            openORnot = self.driver.find_element(By.XPATH,HelperFunc.load("locators/request_cert/requestcert_page.json").get("usage")).get_attribute("class")
            if "ng-select-opened"  not in  openORnot:
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/request_cert/requestcert_page.json").get("usage")).click()
                time.sleep(2)
                HelperFunc.extract_xpaths(self.driver,"locators/request_cert/requestcert_page.json")
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/request_cert/requestcert_page.json").get(str(HelperFunc.search_in_json_file(0,1,"locators/request_cert/requestcert_page.json",0)))).click()
                HelperFunc.save_results("Test 7 RequestCert : usage picked status")
                
            else:
                HelperFunc.extract_xpaths(self.driver,"locators/request_cert/requestcert_page.json")
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/request_cert/requestcert_page").get(str(HelperFunc.search_in_json_file(0,1,"locators/request_cert/requestcert_page.json",0)))).click()
                HelperFunc.save_results("Test 7 RequestCert : usage picked status")
                
    def click_submit_RequestCert(self):
        for _ in range(20):
            self.driver.find_element(By.TAG_NAME,'body').send_keys(Keys.ARROW_DOWN)
            time.sleep(0.2)
        time.sleep(1)
        self.driver.find_element(By.XPATH,HelperFunc.load("locators/request_cert/requestcert_page.json").get("submit")).click()
        WebDriverWait(self.driver, 60).until(EC.url_changes(self.driver.current_url))
        HelperFunc.save_results("Test 7 RequestCert : submit button clicked status")
        WebDriverWait(self.driver, 180).until(EC.invisibility_of_element_located((By.ID, "loading")))
        HelperFunc.save_results("Test 7 RequestCert : requests send status")
    
    def aprove_request_micro(self):
        time.sleep(20)
        if "/#/certificate-request/list" in self.driver.current_url:
            HelperFunc.extract_xpaths(self.driver,"locators/request_cert/requestcert_page.json")
            self.driver.find_element(By.XPATH,HelperFunc.load("locators/request_cert/requestcert_page.json").get("approve_btn")).click()
            HelperFunc.save_results("Test 7 RequestCert : aprove button clicked status")
            time.sleep(2)
            HelperFunc.extract_xpaths(self.driver,"locators/request_cert/requestcert_page.json")
            self.driver.find_element(By.XPATH,HelperFunc.load("locators/request_cert/requestcert_page.json").get("swal2-confirm swal2-styled")).click()
            HelperFunc.save_results("Test 7 RequestCert : aprove button second clicked status")
            HelperFunc.save_results("Test 7 RequestCert : waiting for aprove status")
            time.sleep(60)
            self.driver.refresh()
            x = 1
            while x>0 :            
                try:
                    self.driver.refresh()
                    time.sleep(15)
                    self.driver.find_element(By.XPATH,'//*[@id="check_btn"][1]').click()
                    HelperFunc.save_results("Test 7 RequestCert : aprove button third clicked status")
                    time.sleep(60)
                    acces=True
                    print("RequestCert : waiting get cert clicked status")
                    break
                except Exception as e:
                    x-=1
        
            
    def aprove_request_ejb(self):
        time.sleep(20)
        if "/#/certificate-request/list" in self.driver.current_url:
            HelperFunc.extract_xpaths(self.driver,"locators/request_cert/requestcert_page.json")
            self.driver.find_element(By.XPATH,HelperFunc.load("locators/request_cert/requestcert_page.json").get("approve_btn")).click()
            HelperFunc.save_results("Test 7 RequestCert : aprove button clicked status")
            time.sleep(2)
            HelperFunc.extract_xpaths(self.driver,"locators/request_cert/requestcert_page.json")
            self.driver.find_element(By.XPATH,HelperFunc.load("locators/request_cert/requestcert_page.json").get("swal2-confirm swal2-styled")).click()
            HelperFunc.save_results("Test 7 RequestCert : aprove button second clicked status")
            HelperFunc.save_results("Test 7 RequestCert : waiting for aprove status")
            time.sleep(60)
            self.driver.refresh()
            
            
                    