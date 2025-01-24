from selenium.webdriver.common.by import By
from ...helpers.helpers import HelperFunc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from ...data.UserData import *
from selenium.webdriver.common.keys import Keys


class CreatePage_usage:
    def __init__(self,driver) -> None:
        self.driver = driver
        if "/#/usage/create" not in driver.current_url:
            raise Exception("You are not on the usage page")
        HelperFunc.clean("locators/usage/create_page.json")
        HelperFunc.extract_xpaths(driver,"locators/usage/create_page.json")
        HelperFunc.save_results("Test 6 usage : extract create page xpaths status")
    
    def enter_name_usage(self):
        if "/#/usage/create" in self.driver.current_url:
            self.driver.find_element(By.XPATH,HelperFunc.load("locators/usage/create_page.json").get("name")).send_keys(usage_name)
            HelperFunc.save_results("Test 6 usage : enter name status")

    def pick_pkiType_Microsoft(self):
        if "/#/usage/create" in self.driver.current_url:
            openORnot = self.driver.find_element(By.XPATH,HelperFunc.load("locators/usage/create_page.json").get("pkiType")).get_attribute("class")
            if "ng-select-opened"  not in  openORnot:
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/usage/create_page.json").get("pkiType")).click()
                time.sleep(2)
                HelperFunc.extract_xpaths(self.driver,"locators/usage/create_page.json")
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/usage/create_page.json").get(str(HelperFunc.search_in_json_file(2,1,"locators/usage/create_page.json",0)))).click()
                HelperFunc.save_results("Test 6 usage : pick pkiType status")
                time.sleep(2)
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/usage/create_page.json").get("pki")).click()
                HelperFunc.extract_xpaths(self.driver,"locators/usage/create_page.json")
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/usage/create_page.json").get(str(HelperFunc.search_in_json_file(0,1,"locators/usage/create_page.json",-1)))).click()
                HelperFunc.save_results("Test 6 usage : pick pki status")
                
            else:
                HelperFunc.extract_xpaths(self.driver,"locators/usage/create_page.json")
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/usage/create_page.json").get(str(HelperFunc.search_in_json_file(2,1,"locators/usage/create_page.json",0)))).click()
                HelperFunc.save_results("Test 6 usage : pick pkiType status")
                time.sleep(2)
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/usage/create_page.json").get("pki")).click()
                HelperFunc.extract_xpaths(self.driver,"locators/usage/create_page.json")
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/usage/create_page.json").get(str(HelperFunc.search_in_json_file(0,1,"locators/usage/create_page.json",-1)))).click()

    def pick_certificate_Authority_Microsoft(self):
        if "/#/usage/create" in self.driver.current_url:
            openORnot = self.driver.find_element(By.XPATH,HelperFunc.load("locators/usage/create_page.json").get("certificateAuthority")).get_attribute("class")
            if "ng-select-opened"  not in  openORnot:
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/usage/create_page.json").get("certificateAuthority")).click()
                time.sleep(2)
                HelperFunc.extract_xpaths(self.driver,"locators/usage/create_page.json")
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/usage/create_page.json").get(str(HelperFunc.search_in_json_file(0,1,"locators/usage/create_page.json",-1)))).click()
                HelperFunc.save_results("Test 6 usage : pick certificate_Authority status")
                
            else:
                HelperFunc.extract_xpaths(self.driver,"locators/usage/create_page.json")
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/usage/create_page.json").get(str(HelperFunc.search_in_json_file(0,1,"locators/usage/create_page.json",-1)))).click()
                HelperFunc.save_results("Test 6 usage : pick certificate_Authority status")

    def pick_certificate_Profile_Microsoft(self):
        if "/#/usage/create" in self.driver.current_url:
            openORnot = self.driver.find_element(By.XPATH,HelperFunc.load("locators/usage/create_page.json").get("certificateProfiles")).get_attribute("class")
            if "ng-select-opened"  not in  openORnot:
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/usage/create_page.json").get("certificateProfiles")).click()
                time.sleep(2)
                HelperFunc.extract_xpaths(self.driver,"locators/usage/create_page.json")
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/usage/create_page.json").get(str(HelperFunc.search_in_json_file(4,1,"locators/usage/create_page.json",-1)))).click()
                HelperFunc.save_results("Test 6 usage : pick certificate_Profile status")
                
            else:
                HelperFunc.extract_xpaths(self.driver,"locators/usage/create_page.json")
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/usage/create_page.json").get(str(HelperFunc.search_in_json_file(4,1,"locators/usage/create_page.json",-1)))).click()
                HelperFunc.save_results("Test 6 usage : pick certificate_Profile status")


    def pick_security_Policy_Microsoft(self):
        if "/#/usage/create" in self.driver.current_url:
            openORnot = self.driver.find_element(By.XPATH,HelperFunc.load("locators/usage/create_page.json").get("securityPolicy")).get_attribute("class")
            if "ng-select-opened"  not in  openORnot:
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/usage/create_page.json").get("securityPolicy")).click()
                time.sleep(2)
                HelperFunc.extract_xpaths(self.driver,"locators/usage/create_page.json")
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/usage/create_page.json").get(str(HelperFunc.search_in_json_file(0,1,"locators/usage/create_page.json",-1)))).click()
                HelperFunc.save_results("Test 6 usage : pick security_Policy status")
                
            else:
                HelperFunc.extract_xpaths(self.driver,"locators/usage/create_page.json")
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/usage/create_page.json").get(str(HelperFunc.search_in_json_file(0,1,"locators/usage/create_page.json",-1)))).click()
                HelperFunc.save_results("Test 6 usage : pick security_Policy status")


    def pick_pkiType_Ejbcace(self):
        if "/#/usage/create" in self.driver.current_url:
            openORnot = self.driver.find_element(By.XPATH,HelperFunc.load("locators/usage/create_page.json").get("pkiType")).get_attribute("class")
            if "ng-select-opened"  not in  openORnot:
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/usage/create_page.json").get("pkiType")).click()
                time.sleep(2)
                HelperFunc.extract_xpaths(self.driver,"locators/usage/create_page.json")
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/usage/create_page.json").get(str(HelperFunc.search_in_json_file(1,1,"locators/usage/create_page.json",0)))).click()
                HelperFunc.save_results("Test 6 usage : pick pkiType status")
                time.sleep(2)
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/usage/create_page.json").get("pki")).click()
                HelperFunc.extract_xpaths(self.driver,"locators/usage/create_page.json")
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/usage/create_page.json").get(str(HelperFunc.search_in_json_file(0,1,"locators/usage/create_page.json",1)))).click()
                HelperFunc.save_results("Test 6 usage : pick pki status")
                
            else:
                HelperFunc.extract_xpaths(self.driver,"locators/usage/create_page.json")
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/usage/create_page.json").get(str(HelperFunc.search_in_json_file(1,1,"locators/usage/create_page.json",0)))).click()
                HelperFunc.save_results("Test 6 usage : pick pkiType status")
                time.sleep(2)
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/usage/create_page.json").get("pki")).click()
                HelperFunc.extract_xpaths(self.driver,"locators/usage/create_page.json")
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/usage/create_page.json").get(str(HelperFunc.search_in_json_file(0,1,"locators/usage/create_page.json",1)))).click()
    
    def pick_End_entity_profile_Ejbcace(self):
        if "/#/usage/create" in self.driver.current_url:
            openORnot = self.driver.find_element(By.XPATH,HelperFunc.load("locators/usage/create_page.json").get("endEntityProfile")).get_attribute("class")
            if "ng-select-opened"  not in  openORnot:
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/usage/create_page.json").get("endEntityProfile")).click()
                time.sleep(2)
                HelperFunc.extract_xpaths(self.driver,"locators/usage/create_page.json")
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/usage/create_page.json").get(str(HelperFunc.search_in_json_file(5,1,"locators/usage/create_page.json",-1)))).click()
                HelperFunc.save_results("Test 6 usage : pick End_entity_profile status")
                
            else:
                HelperFunc.extract_xpaths(self.driver,"locators/usage/create_page.json")
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/usage/create_page.json").get(str(HelperFunc.search_in_json_file(5,1,"locators/usage/create_page.json",-1)))).click()
                HelperFunc.save_results("Test 6 usage : pick End_entity_profile status")
    
    def pick_certificate_Authority_Ejbcace(self):
        if "/#/usage/create" in self.driver.current_url:
            openORnot = self.driver.find_element(By.XPATH,HelperFunc.load("locators/usage/create_page.json").get("certificateAuthority")).get_attribute("class")
            if "ng-select-opened"  not in  openORnot:
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/usage/create_page.json").get("certificateAuthority")).click()
                time.sleep(2)
                HelperFunc.extract_xpaths(self.driver,"locators/usage/create_page.json")
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/usage/create_page.json").get(str(HelperFunc.search_in_json_file(2,1,"locators/usage/create_page.json",-1)))).click()
                HelperFunc.save_results("Test 6 usage : pick certificate_Authority status")
                
            else:
                HelperFunc.extract_xpaths(self.driver,"locators/usage/create_page.json")
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/usage/create_page.json").get(str(HelperFunc.search_in_json_file(2,1,"locators/usage/create_page.json",-1)))).click()
                HelperFunc.save_results("Test 6 usage : pick certificate_Authority status")

    def pick_certificate_Profile_Ejbcace(self):
        if "/#/usage/create" in self.driver.current_url:
            openORnot = self.driver.find_element(By.XPATH,HelperFunc.load("locators/usage/create_page.json").get("certificateProfiles")).get_attribute("class")
            if "ng-select-opened"  not in  openORnot:
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/usage/create_page.json").get("certificateProfiles")).click()
                time.sleep(2)
                HelperFunc.extract_xpaths(self.driver,"locators/usage/create_page.json")
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/usage/create_page.json").get(str(HelperFunc.search_in_json_file(1,1,"locators/usage/create_page.json",-1)))).click()
                HelperFunc.save_results("Test 6 usage : pick certificate_Profile status")
                
            else:
                HelperFunc.extract_xpaths(self.driver,"locators/usage/create_page.json")
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/usage/create_page.json").get(str(HelperFunc.search_in_json_file(1,1,"locators/usage/create_page.json",-1)))).click()
                HelperFunc.save_results("Test 6 usage : pick certificate_Profile status")


    def pick_security_Policy_Ejbcace(self):
        if "/#/usage/create" in self.driver.current_url:
            openORnot = self.driver.find_element(By.XPATH,HelperFunc.load("locators/usage/create_page.json").get("securityPolicy")).get_attribute("class")
            if "ng-select-opened"  not in  openORnot:
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/usage/create_page.json").get("securityPolicy")).click()
                time.sleep(2)
                HelperFunc.extract_xpaths(self.driver,"locators/usage/create_page.json")
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/usage/create_page.json").get(str(HelperFunc.search_in_json_file(0,1,"locators/usage/create_page.json",-1)))).click()
                HelperFunc.save_results("Test 6 usage : pick security_Policy status")
                
            else:
                HelperFunc.extract_xpaths(self.driver,"locators/usage/create_page.json")
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/usage/create_page.json").get(str(HelperFunc.search_in_json_file(0,1,"locators/usage/create_page.json",-1)))).click()
                HelperFunc.save_results("Test 6 usage : pick security_Policy status")

                        
    def pick_Csr_generation_mode(self):
        self.driver.find_element(By.XPATH,HelperFunc.load("locators/usage/create_page.json").get("Request without CSR")).click()
        HelperFunc.save_results("Test 6 usage : pick Csr_generation_mode status")

    def pick_Default_csr_generation_mode(self):
        if "/#/usage/create" in self.driver.current_url:
            openORnot = self.driver.find_element(By.XPATH,HelperFunc.load("locators/usage/create_page.json").get("defaultGenerationMode")).get_attribute("class")
            if "ng-select-opened"  not in  openORnot:
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/usage/create_page.json").get("defaultGenerationMode")).click()
                time.sleep(2)
                HelperFunc.extract_xpaths(self.driver,"locators/usage/create_page.json")
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/usage/create_page.json").get(str(HelperFunc.search_in_json_file(0,1,"locators/usage/create_page.json",-1)))).click()
                HelperFunc.save_results("Test 6 usage : pick Default_csr_generation status")
                
            else:
                HelperFunc.extract_xpaths(self.driver,"locators/usage/create_page.json")
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/usage/create_page.json").get(str(HelperFunc.search_in_json_file(0,1,"locators/usage/create_page.json",-1)))).click()
                HelperFunc.save_results("Test 6 usage : pick Default_csr_generation status")

    def scroll_by_pressing_down(self):
        for _ in range(20):
            self.driver.find_element(By.TAG_NAME,'body').send_keys(Keys.ARROW_DOWN)
            time.sleep(0.2)

    def pick_Certificate_DN_mode(self):
        if "/#/usage/create" in self.driver.current_url:
            openORnot = self.driver.find_element(By.XPATH,HelperFunc.load("locators/usage/create_page.json").get("distinguishedName")).get_attribute("class")
            if "ng-select-opened"  not in  openORnot:
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/usage/create_page.json").get("distinguishedName")).click()
                time.sleep(2)
                HelperFunc.extract_xpaths(self.driver,"locators/usage/create_page.json")
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/usage/create_page.json").get(str(HelperFunc.search_in_json_file(0,1,"locators/usage/create_page.json",-1)))).click()
                HelperFunc.save_results("Test 6 usage : pick Certificate_DN status")
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/usage/create_page.json").get("addDistinguishedName")).click()
                HelperFunc.save_results("Test 6 usage : add DN status")
                HelperFunc.extract_xpaths(self.driver,"locators/usage/create_page.json")
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/usage/create_page.json").get("commonName")).send_keys("NG")
                HelperFunc.save_results("Test 6 usage : add common name status")

            else:
                HelperFunc.extract_xpaths(self.driver,"locators/usage/create_page.json")
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/usage/create_page.json").get(str(HelperFunc.search_in_json_file(0,1,"locators/usage/create_page.json",-1)))).click()
                HelperFunc.save_results("Test 6 usage : pick Certificate_DN status")
                HelperFunc.extract_xpaths(self.driver,"locators/usage/create_page.json")
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/usage/create_page.json").get("commonName")).send_keys("NG")
                HelperFunc.save_results("Test 6 usage : add common name status")

    def pick_Certificate_DN_mode_2(self):
        if "/#/usage/create" in self.driver.current_url:
            openORnot = self.driver.find_element(By.XPATH,HelperFunc.load("locators/usage/create_page.json").get("distinguishedName")).get_attribute("class")
            if "ng-select-opened"  not in  openORnot:
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/usage/create_page.json").get("distinguishedName")).click()
                time.sleep(2)
                HelperFunc.extract_xpaths(self.driver,"locators/usage/create_page.json")
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/usage/create_page.json").get(str(HelperFunc.search_in_json_file(0,1,"locators/usage/create_page.json",-1)))).click()
                time.sleep(1)
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/usage/create_page.json").get(str(HelperFunc.search_in_json_file(3,1,"locators/usage/create_page.json",-1)))).click()
                time.sleep(1)
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/usage/create_page.json").get(str(HelperFunc.search_in_json_file(4,1,"locators/usage/create_page.json",-1)))).click()
                time.sleep(1)
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/usage/create_page.json").get(str(HelperFunc.search_in_json_file(5,1,"locators/usage/create_page.json",-1)))).click()
                HelperFunc.save_results("Test 6 usage : pick Certificate_DN status")
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/usage/create_page.json").get("addDistinguishedName")).click()
                HelperFunc.save_results("Test 6 usage : add DN status")
                HelperFunc.extract_xpaths(self.driver,"locators/usage/create_page.json")
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/usage/create_page.json").get("commonName")).send_keys("NG")
                time.sleep(1)
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/usage/create_page.json").get("position-relative")).click()
                time.sleep(1)
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/usage/create_page.json").get("position-relative-0")).click()
                time.sleep(1)
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/usage/create_page.json").get("Enter the organization unit")).send_keys("NG")
                time.sleep(1)
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/usage/create_page.json").get("Enter the organization unit")).send_keys(Keys.ENTER)
                time.sleep(1) 
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/usage/create_page.json").get("position-relative-2")).click()
                time.sleep(1) 
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/usage/create_page.json").get("position-relative-3")).click()
                time.sleep(1)
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/usage/create_page.json").get("Enter the organization")).send_keys("NG")
                time.sleep(1)
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/usage/create_page.json").get("Enter the organization")).send_keys(Keys.ENTER)
                time.sleep(1) 
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/usage/create_page.json").get("position-relative-5")).click()
                time.sleep(1)
                for _ in range(20):
                    self.driver.find_element(By.TAG_NAME,'body').send_keys(Keys.ARROW_DOWN)
                    time.sleep(0.2)
                
                time.sleep(1)
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/usage/create_page.json").get("position-relative-6")).click()
                time.sleep(1)
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/usage/create_page.json").get("Enter the locality")).send_keys("NG")
                time.sleep(1)
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/usage/create_page.json").get("Enter the locality")).send_keys(Keys.ENTER)
                time.sleep(1) 
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/usage/create_page.json").get("position-relative-8")).click()
                time.sleep(1)
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/usage/create_page.json").get("position-relative-9")).click()
                time.sleep(1)
                HelperFunc.save_results("Test 6 usage : add common name status")

    def pick_Certificate_SN_mode_2(self):
        if "/#/usage/create" in self.driver.current_url:
            openORnot = self.driver.find_element(By.XPATH,HelperFunc.load("locators/usage/create_page.json").get("subjectAlternativeName")).get_attribute("class")
            if "ng-select-opened"  not in  openORnot:
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/usage/create_page.json").get("subjectAlternativeName")).click()
                time.sleep(2)
                HelperFunc.extract_xpaths(self.driver,"locators/usage/create_page.json")
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/usage/create_page.json").get(str(HelperFunc.search_in_json_file(0,1,"locators/usage/create_page.json",-1)))).click()
                time.sleep(1)
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/usage/create_page.json").get(str(HelperFunc.search_in_json_file(1,1,"locators/usage/create_page.json",-1)))).click()
                time.sleep(1)
                HelperFunc.save_results("Test 6 usage : pick Certificate_SN status")
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/usage/create_page.json").get("addSubjectAlternativeName")).click()
                HelperFunc.save_results("Test 6 usage : add SN status")
                HelperFunc.extract_xpaths(self.driver,"locators/usage/create_page.json")
                time.sleep(1)
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/usage/create_page.json").get("Enter the DNS")).send_keys("NG")
                time.sleep(1)
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/usage/create_page.json").get("Enter the DNS")).send_keys(Keys.ENTER)
                time.sleep(1) 
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/usage/create_page.json").get("position-relative-11")).click()
                time.sleep(1)
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/usage/create_page.json").get("position-relative-12")).click()
                time.sleep(1)
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/usage/create_page.json").get("Enter additional emails")).send_keys("NG@ng.fr")
                time.sleep(1)
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/usage/create_page.json").get("Enter additional emails")).send_keys(Keys.ENTER)
                time.sleep(1) 
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/usage/create_page.json").get("position-relative-15")).click()
                time.sleep(1) 
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/usage/create_page.json").get("position-relative-16")).click()
                time.sleep(1) 
                
    
    def pick_key_Algo(self):
        if "/#/usage/create" in self.driver.current_url:
            openORnot = self.driver.find_element(By.XPATH,HelperFunc.load("locators/usage/create_page.json").get("keyAlgo")).get_attribute("class")
            if "ng-select-opened"  not in  openORnot:
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/usage/create_page.json").get("keyAlgo")).click()
                time.sleep(2)
                HelperFunc.extract_xpaths(self.driver,"locators/usage/create_page.json")
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/usage/create_page.json").get(str(HelperFunc.search_in_json_file(0,1,"locators/usage/create_page.json",-1)))).click()
                HelperFunc.save_results("Test 6 usage : pick key_Algo status")
                
                
            else:
                HelperFunc.extract_xpaths(self.driver,"locators/usage/create_page.json")
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/usage/create_page.json").get(str(HelperFunc.search_in_json_file(0,1,"locators/usage/create_page.json",-1)))).click()
                HelperFunc.save_results("Test 6 usage : pick key_Algo status")

    def pick_keySize(self):
        if "/#/usage/create" in self.driver.current_url:
            openORnot = self.driver.find_element(By.XPATH,HelperFunc.load("locators/usage/create_page.json").get("keySize")).get_attribute("class")
            if "ng-select-opened"  not in  openORnot:
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/usage/create_page.json").get("keySize")).click()
                time.sleep(2)
                HelperFunc.extract_xpaths(self.driver,"locators/usage/create_page.json")
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/usage/create_page.json").get(str(HelperFunc.search_in_json_file(0,1,"locators/usage/create_page.json",-1)))).click()
                HelperFunc.save_results("Test 6 usage : pick keySize status")
                
            else:
                HelperFunc.extract_xpaths(self.driver,"locators/usage/create_page.json")
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/usage/create_page.json").get(str(HelperFunc.search_in_json_file(0,1,"locators/usage/create_page.json",-1)))).click()
                HelperFunc.save_results("Test 6 usage : pick keySize status")
                time.sleep(2)

    def click_submit_usage(self):
        self.driver.find_element(By.XPATH,HelperFunc.load("locators/usage/create_page.json").get("submit")).click()
        WebDriverWait(self.driver, 60).until(EC.url_changes(self.driver.current_url))
        HelperFunc.save_results("Test 6 usage : submit button click status")
        WebDriverWait(self.driver, 180).until(EC.invisibility_of_element_located((By.ID, "loading")))
        HelperFunc.save_results("Test 6 usage : new usage create status")

    