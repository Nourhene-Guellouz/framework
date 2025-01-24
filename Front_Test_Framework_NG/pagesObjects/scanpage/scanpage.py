from selenium.webdriver.common.by import By
from ...helpers.helpers import HelperFunc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from ...helpers.helpers import HelperFunc
from ...data.UserData import *





class ScanPage:
    def __init__(self,driver) -> None:
        self.driver = driver
        HelperFunc.clean("locators/scan/scan_page.json")

        
    def click_new_scan(self):
        self.driver.find_element(By.XPATH,HelperFunc.load("locators/dashbord/dashbrod_page.json").get("launchScan")).click()
        HelperFunc.save_results("Test 7 scan : Add scan clicked status")
        WebDriverWait(self.driver, 60).until(EC.url_changes(self.driver.current_url))
        WebDriverWait(self.driver, 180).until(EC.invisibility_of_element_located((By.ID, "loading")))
        HelperFunc.save_results("Test 7 scan : acces scan clicked status")
        if "/#/task/scan-choice" in self.driver.current_url:
            HelperFunc.extract_xpaths(self.driver,"locators/scan/scan_page.json")
            self.driver.find_element(By.XPATH,HelperFunc.load("locators/scan/scan_page.json").get("newScan")).click()
            HelperFunc.save_results("Test 7 scan : new scan clicked status")
            WebDriverWait(self.driver, 60).until(EC.url_changes(self.driver.current_url))
            WebDriverWait(self.driver, 180).until(EC.invisibility_of_element_located((By.ID, "loading")))
            HelperFunc.save_results("Test 7 scan : new scan clicked status")

    def enter_name_scan(self):
        if "/#/task/single-create?action=launch" in self.driver.current_url:
            HelperFunc.extract_xpaths(self.driver,"locators/scan/scan_page.json")
            time.sleep(2)
            self.driver.find_element(By.XPATH,HelperFunc.load("locators/scan/scan_page.json").get("name")).send_keys(apache97_name)
            HelperFunc.save_results("Test 7 scan : enter name status")

    def pick_scan_type(self):
        if "/#/task/single-create?action=launch" in self.driver.current_url:
            openORnot = self.driver.find_element(By.XPATH,HelperFunc.load("locators/scan/scan_page.json").get("taskTypes")).get_attribute("class")
            if "ng-select-opened"  not in  openORnot:
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/scan/scan_page.json").get("taskTypes")).click()
                time.sleep(2)
                HelperFunc.extract_xpaths(self.driver,"locators/scan/scan_page.json")
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/scan/scan_page.json").get(str(HelperFunc.search_in_json_file(2,1,"locators/scan/scan_page.json",0)))).click()
                HelperFunc.save_results("Test 7 scan : scan picked status")
                
            else:
                HelperFunc.extract_xpaths(self.driver,"locators/scan/scan_page.json")
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/scan/scan_page.json").get(str(HelperFunc.search_in_json_file(2,1,"locators/scan/scan_page.json",0)))).click()
                HelperFunc.save_results("Test 7 scan : scan picked status")
                
    def pick_scannerServer(self):
        if "/#/task/single-create?action=launch" in self.driver.current_url:
            HelperFunc.extract_xpaths(self.driver,"locators/scan/scan_page.json")
            time.sleep(3)
            openORnot = self.driver.find_element(By.XPATH,HelperFunc.load("locators/scan/scan_page.json").get("scannerServer")).get_attribute("class")
            if "ng-select-opened"  not in  openORnot:
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/scan/scan_page.json").get("scannerServer")).click()
                time.sleep(2)
                HelperFunc.extract_xpaths(self.driver,"locators/scan/scan_page.json")
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/scan/scan_page.json").get(str(HelperFunc.search_in_json_file(0,1,"locators/scan/scan_page.json",-1)))).click()
                HelperFunc.save_results("Test 7 scan : scannerServer picked status")
                
            else:
                HelperFunc.extract_xpaths(self.driver,"locators/scan/scan_page.json")
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/scan/scan_page.json").get(str(HelperFunc.search_in_json_file(0,1,"locators/scan/scan_page.json",-1)))).click()
                HelperFunc.save_results("Test 7 scan : scannerServer picked status")

    def pick_applicationType(self):
        if "/#/task/single-create?action=launch" in self.driver.current_url:
            ScanPage.pick_scan_type(self)
            openORnot = self.driver.find_element(By.XPATH,HelperFunc.load("locators/scan/scan_page.json").get("applicationType")).get_attribute("class")
            if "ng-select-opened"  not in  openORnot:
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/scan/scan_page.json").get("applicationType")).click()
                time.sleep(2)
                HelperFunc.extract_xpaths(self.driver,"locators/scan/scan_page.json")
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/scan/scan_page.json").get(str(HelperFunc.search_in_json_file(0,1,"locators/scan/scan_page.json",-1)))).click()
                HelperFunc.save_results("Test 7 scan : applicationType picked status")
                
            else:
                HelperFunc.extract_xpaths(self.driver,"locators/scan/scan_page.json")
                self.driver.find_element(By.XPATH,HelperFunc.load("locators/scan/scan_page.json").get(str(HelperFunc.search_in_json_file(0,1,"locators/scan/scan_page.json",-1)))).click()
                HelperFunc.save_results("Test 7 scan : applicationType picked status")
                
    def click_submit_scan(self):
        time.sleep(3)
        HelperFunc.extract_xpaths(self.driver,"locators/scan/scan_page.json")
        time.sleep(2)
        self.driver.find_element(By.XPATH,HelperFunc.load("locators/scan/scan_page.json").get("submit")).click()
        WebDriverWait(self.driver, 60).until(EC.url_changes(self.driver.current_url))
        HelperFunc.save_results("Test 7 scan : submit button clicked status")
        WebDriverWait(self.driver, 180).until(EC.invisibility_of_element_located((By.ID, "loading")))
        HelperFunc.save_results("Test 7 scan : scan send status")
    