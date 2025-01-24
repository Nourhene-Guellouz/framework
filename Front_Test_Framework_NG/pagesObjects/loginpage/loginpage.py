from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import  StaleElementReferenceException, NoSuchElementException
from ...helpers.helpers import HelperFunc
import time
class LoginPage:
    def __init__(self,driver) -> None:
        self.driver = driver
        time.sleep(10)
        if "/#/login" not in driver.current_url:
            raise Exception("You are not on the login page")
        HelperFunc.save_results("Test 1 login : url acces status")
        HelperFunc.extract_xpaths(driver,"locators/login/login_page.json")
        HelperFunc.save_results("Test 1 login : extract xpaths status")
    def enter_username(self,username):
        if "/#/login" in self.driver.current_url:
            self.driver.find_element(By.XPATH,HelperFunc.load("locators/login/login_page.json").get("emailInput")).clear()
            self.driver.implicitly_wait(10)
            self.driver.find_element(By.XPATH,HelperFunc.load("locators/login/login_page.json").get("emailInput")).send_keys(username)
            HelperFunc.save_results("Test 1 login : entre username status")
    def enter_password(self,password):
        if "/#/login" in self.driver.current_url:
            self.driver.find_element(By.XPATH,HelperFunc.load("locators/login/login_page.json").get("passwordInput")).clear()
            self.driver.implicitly_wait(10)
            self.driver.find_element(By.XPATH,HelperFunc.load("locators/login/login_page.json").get("passwordInput")).send_keys(password)
            HelperFunc.save_results("Test 1 login : entre password status")
    def click_login(self):
        self.driver.implicitly_wait(10)
        try:
            if "/#/login" in self.driver.current_url:
                signin_button = self.driver.find_element(By.XPATH,HelperFunc.load("locators/login/login_page.json").get("signin"))
                signin_button.click()
                WebDriverWait(self.driver, 60).until(EC.url_changes(self.driver.current_url))
                HelperFunc.save_results("Test 1 login : login button clicking status")
                WebDriverWait(self.driver, 180).until(EC.invisibility_of_element_located((By.ID, "loading")))
                HelperFunc.save_results("Test 1 login : acess dashbord page status")
                
        except (StaleElementReferenceException, NoSuchElementException):
            print("Element not found")