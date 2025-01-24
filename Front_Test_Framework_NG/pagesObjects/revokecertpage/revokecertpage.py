from selenium.webdriver.common.by import By
from ...helpers.helpers import HelperFunc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from ...helpers.helpers import HelperFunc





class RevokecertPage:
    def __init__(self,driver) -> None:
        self.driver = driver
        
        
    
    def click_dropdown_side_certificates(self):
        HelperFunc.save_results("Test 8 RevokeCert : Dropdown clicked status")
        self.driver.find_element(By.XPATH,HelperFunc.load("locators/dashbord/dashbrod_page.json").get("certificates")).click()
        HelperFunc.save_results("Test 8 RevokeCert : Certificates clicked status")
        WebDriverWait(self.driver, 60).until(EC.url_changes(self.driver.current_url))
        WebDriverWait(self.driver, 180).until(EC.invisibility_of_element_located((By.ID, "loading")))
        HelperFunc.save_results("Test 8 RevokeCert : acces Certificates clicked status")

    def revoke_cert(self):
        time.sleep(5)
        self.driver.find_element(By.XPATH,HelperFunc.load("locators/revoke_cert/revokecer_page.json").get("1-moreCertificate")).click()
        HelperFunc.save_results("Test 8 RevokeCert : More button clicked status")
        time.sleep(5)
        self.driver.find_element(By.XPATH,HelperFunc.load("locators/revoke_cert/revokecer_page.json").get("1-revokeCertificate")).click()
        HelperFunc.save_results("Test 8 RevokeCert : Revoke button clicked status")
        time.sleep(5)
        self.driver.find_element(By.XPATH,HelperFunc.load("locators/revoke_cert/revokecer_page.json").get("swal2-confirm swal2-styled")).click()
        HelperFunc.save_results("Test 8 RevokeCert : Revoke confirm button clicked status")
        time.sleep(5)
        self.driver.find_element(By.XPATH,HelperFunc.load("locators/revoke_cert/revokecer_page.json").get("swal2-confirm swal2-styled")).click()
        HelperFunc.save_results("Test 8 RevokeCert : Revoke confirm button clicked status")

    def click_dropdown_side_revokes(self):
        self.driver.find_element(By.XPATH,HelperFunc.load("locators/dashbord/dashbrod_page.json").get("requestsDropdown")).click()
        HelperFunc.save_results("Test 8 RevokeCert : Dropdown sidebar clicked status")
        time.sleep(5)
        self.driver.find_element(By.XPATH,HelperFunc.load("locators/dashbord/dashbrod_page.json").get("revocationRequests")).click()
        HelperFunc.save_results("Test 8 RevokeCert : Revoke sidebar clicked status")
        WebDriverWait(self.driver, 60).until(EC.url_changes(self.driver.current_url))
        WebDriverWait(self.driver, 180).until(EC.invisibility_of_element_located((By.ID, "loading")))
        HelperFunc.save_results("Test 8 RevokeCert : acces Revoke sidebar clicked status")
    
    def approve_revoke(self):
        self.driver.find_element(By.XPATH,HelperFunc.load("locators/revoke_cert/revokecer_page.json").get("btn btn-sm btn-outline-primary")).click()
        HelperFunc.save_results("Test 8 RevokeCert : Approve button in revoke page clicked status")
        time.sleep(5)
        self.driver.find_element(By.XPATH,HelperFunc.load("locators/revoke_cert/revokecer_page.json").get("swal2-confirm swal2-styled")).click()
        HelperFunc.save_results("Test 8 RevokeCert : Approve button in revoke page clicked status")
        time.sleep(5)
        