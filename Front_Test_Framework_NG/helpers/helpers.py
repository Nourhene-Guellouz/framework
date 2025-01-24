from selenium import webdriver
import json, time
from selenium.webdriver.common.by import By
from .extract_script import absolute_xpath_script
from ..data.UserData import *
import requests
import warnings

warnings.filterwarnings("ignore", message="Unverified HTTPS request")

class HelperFunc:
    
    def __init__():
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option('prefs', {'intl.accept_languages': 'en'})
        chrome_options.add_argument('--ignore-ssl-errors=yes')
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_argument("--window-size=1920,1080")  
        chrome_options.add_argument("--force-device-scale-factor=0.5")
        #chrome_options.add_argument("--headless")  # Runs Chrome in headless mode
        driver = webdriver.Chrome(options=chrome_options);
        driver.maximize_window()
        return driver
    
    def search_in_json_file(element,option,path,index=None):
        if option==1:
            with open(full_path+path, "r") as file:
                json_data = json.load(file)
                matching_keys = HelperFunc.find_keys(json_data,element)
                return matching_keys[index]
        if option==2:
            with open(full_path+path, "r") as file:
                json_data = json.load(file)
                matching_keys = HelperFunc.find_all_keys(json_data)
                return matching_keys[index]
    
    def find_last_key(data):
        last_key =[]
        if isinstance(data, dict):
            for key in data.keys():
                if isinstance(key, str) and key.startswith('a') and key.count('-') == 1:
                    parts = key.split('-')
                    if len(parts[1]) == 1:
                        last_key.append(parts[0]+'-'+str(int(parts[1])))    
        return last_key

    def find_all_keys(data):
        keys_matching_criteria = []
        if isinstance(data, dict):
            for key, value in data.items():  # Corrected the iteration to unpack key-value pairs
                if isinstance(key, str) and key.startswith('a') and key.count('-') == 1 and ((len(key) == 14) or (len(key) == 12)):
                    keys_matching_criteria.append(key)
        return keys_matching_criteria
    
    def find_keys(data, element):
        keys_matching_criteria = []
        if isinstance(data, dict):
            for key, value in data.items():  # Corrected the iteration to unpack key-value pairs
                if isinstance(key, str) and key.startswith('a') and key.endswith('-' + str(element)) and ((len(key) == 14) or (len(key) == 12)):
                    keys_matching_criteria.append(key)
        return keys_matching_criteria

    
    def extract_xpaths(driver,page_name):
        time.sleep(5)
        all_elements = driver.find_elements(By.XPATH, "//*")
        elements_xpath = {}
        x=0
        span_tag=0

        for element in all_elements:
            xpath = driver.execute_script(absolute_xpath_script, element)
            if(element.tag_name not in ["script","style","head","meta","link","title","base","noscript","router-outlet"]):
                if element.get_attribute("id") and element.get_attribute("id").strip() != "":
                    role=False
                    rolex=0
                    roledata=str(element.get_attribute("id"))
                    while role==False:
                        if roledata not in elements_xpath:
                            elements_xpath[roledata] = xpath
                            role=True
                        else:
                            roledata=str(element.get_attribute("id"))+"-"+str(rolex)
                            rolex=rolex+1
                elif element.get_attribute("name") and element.get_attribute("name").strip() != "":
                    elements_xpath[element.get_attribute("name")] = xpath
                elif element.get_attribute("value") and element.get_attribute("value").strip() != "":
                    elements_xpath[element.get_attribute("value")] = xpath
                elif element.get_attribute("placeholder") and element.get_attribute("placeholder").strip() != "":
                    elements_xpath[element.get_attribute("placeholder")] = xpath
                elif element.get_attribute("alt") and element.get_attribute("alt").strip() != "":
                    elements_xpath[element.get_attribute("alt")] = xpath
                elif element.get_attribute("role") and element.get_attribute("role").strip() != "":
                    role=False
                    rolex=0
                    roledata=str(element.get_attribute("role"))
                    while role==False:
                        if roledata not in elements_xpath:
                            elements_xpath[roledata] = xpath
                            role=True
                        else:
                            roledata=str(element.get_attribute("role"))+"-"+str(rolex)
                            rolex=rolex+1
                elif element.get_attribute("class") and element.get_attribute("class").strip() != "":
                    if(str(element.tag_name)=="span"):
                        span_tag=span_tag+1
                        elements_xpath[str(element.get_attribute("innerText"))+str(element.tag_name)] = xpath
                    else:
                        role=False
                        rolex=0
                        roledata=str(element.get_attribute("class"))
                        while role==False:
                            if roledata not in elements_xpath:
                                elements_xpath[roledata] = xpath
                                role=True
                            else:
                                roledata=str(element.get_attribute("class"))+"-"+str(rolex)
                                rolex=rolex+1
                elif element.text and element.text.strip() != "":
                    elements_xpath[element.text.strip()] = xpath
                else:
                    if(str(element.tag_name)=="span"):
                        span_tag=span_tag+1
                        elements_xpath[str(element.tag_name)+str(span_tag)] = xpath
                    else:
                        x=x+1
                        elements_xpath[str(element.tag_name)+str(x)] = xpath
        try:
            with open(full_path+page_name, "r") as json_file:
                data = json.load(json_file)
        except FileNotFoundError:
            data = {}

        merged_dict = {**data, **elements_xpath}
        HelperFunc.save(page_name,merged_dict)

    def save(path,merged_dict):
        with open(full_path+path, "w") as json_file:
            json.dump(merged_dict, json_file, indent=4)
        
    def clean(path):
        with open(full_path+path, "w") as json_file:
            json.dump({}, json_file, indent=4)
        
    def init_results(i):
        with open(full_path+"db/results.json", "w") as json_file:
            json.dump({}, json_file, indent=4)
        if i=="0":
            with open(full_path+"db/micro.json", "r") as json_file:
                elements_xpath = json.load(json_file)
        elif i=="1":
            with open(full_path+"db/ejbcace.json", "r") as json_file:
                elements_xpath = json.load(json_file)
        elif i=="2":
            with open(full_path+"db/apache97.json", "r") as json_file:
                elements_xpath = json.load(json_file)
        for element in elements_xpath.keys():
            elements_xpath[element] = "0"
        with open(full_path+"db/results.json", "w") as json_file:
            json.dump(elements_xpath, json_file, indent=4)

    
         
    def save_results(element):
        with open(full_path+"db/results.json", "r") as json_file:
            elements_xpath = json.load(json_file)
        elements_xpath[element] = "1"
        print(element)
        with open(full_path+"db/results.json", "w") as json_file:
            json.dump(elements_xpath, json_file, indent=4)
         
    def load(path):
        with open(full_path+path, "r") as json_file:
            elements_xpath = json.load(json_file)
        return elements_xpath       
    
    def verfiy_pki_sync_(driver):
        HelperFunc.save_results("Test 5 sync : check if the pki is synced")
        time.sleep(60)
        repeate=5
        cookies = driver.get_cookies()
        
        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json; charset=utf-8',
            'Cookie': f'Token={str(cookies[2]["value"])}; RefreshToken={str(cookies[1]["value"])}',
            
        }
        sync=False
        while repeate>0:
            logs_url = url+f'bcs-berrynotify/api/v1/activity_events/?page=1&size=20&sort=id,asc&tenant__in={tenant_name}&&frontVersion=dev-version'
            response = requests.get(logs_url, headers=headers, verify=False)
            v=0
            index=0
            for i in range(len(response.json())):
                if response.json()[i]['name']=="SYNC_PKI":
                    index=i
                    break 
            
            l=7
            for i in range(len(response.json()[index]["activity_steps"])):
                if (response.json()[index]["activity_steps"][i]["status"]) == "SUCCEEDED":
                    v=v+1
                        
            if(l==v or l==v+1):
                sync=True
                break
            else:
                print("Test 5 sync : pki is not synced yet")
                time.sleep(30)
                repeate-=1

        if sync==True:
            HelperFunc.save_results("Test 5 sync : pki is synced")
            return True
        else:
            HelperFunc.save_results("Test 5 sync : pki is not synced")
            return False
        
    def get_pki_tosync(json_data, substring):
        keys_with_substring = []
        if isinstance(json_data, dict):
            for key in json_data:
                if str(substring) in str(key):
                    keys_with_substring.append(key)
        return keys_with_substring
    
    def delete_tenant(driver):
        
             
        cookies = driver.get_cookies()
        
        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json; charset=utf-8',
            'Cookie': f'Token={str(cookies[2]["value"])}; RefreshToken={str(cookies[1]["value"])}',
            
        }
        try:
            
            url1 = url+f'api/v1/tenants/?name={tenant_name}&frontVersion=dev-version'
            r = requests.get(url1, headers=headers, verify=False)
        except requests.RequestException as e:
            pass
        
        try:
            id = r.json()[0]['id']
            url2 = url+f'api/v1/tenants/{id}/'
            r = requests.delete(url2, headers=headers, verify=False)
        
        except requests.RequestException as e:
            pass
        HelperFunc.save_results("Test 6 delete : delete tenant status")
    
    def extract_xpaths__short_xpath(driver,page_name):
        time.sleep(5)
        all_elements = driver.find_elements(By.XPATH, "//*")
        elements_xpath = {}
        for element in all_elements:
            html_snippet = element.get_attribute("outerHTML")
            # Filter out elements with header tags
            if html_snippet and element.tag_name.lower() in ["h1", "h2", "h2", "h3", "h4","h5","h6","a","span","div","select","button"]:
                element_id = element.get_attribute("id")
                element_class = element.get_attribute("class")
                if element_id:
                    xpath = f"//*[@id='{element_id}']"
                    # Remove backslashes from html_snippet
                    html_snippet = html_snippet.replace("\\", "")
                    # Truncate the html_snippet if it's too long
                    max_length = 1000  # Adjust the maximum length as needed
                    if len(html_snippet) > max_length:
                        html_snippet = html_snippet[:max_length] + "..."
                    elements_xpath[element_id] = xpath
                elif element_class:
                    xpath = f"//*[@class='{element_class}']"
                    elements_xpath[element_class] = xpath
        try:
            with open(full_path+page_name, "r") as json_file:
                data = json.load(json_file)
        except FileNotFoundError:
            data = {}

        merged_dict = {**data, **elements_xpath}
        HelperFunc.save(page_name,merged_dict)



