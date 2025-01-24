
from ...helpers.helpers import *
import time
from ...data.UserData import username, password , url
from ...pagesObjects.loginpage.loginpage import *
from ...pagesObjects.dashbord.dashbord import *
from ...pagesObjects.credentialspage.credentialpage import *
from ...pagesObjects.credentialspage.createpage import *
from ...pagesObjects.pkipage.pkipage import *
from ...pagesObjects.pkipage.createpage import *
from ...pagesObjects.usagepage.usagepage import *
from ...pagesObjects.usagepage.createpage import *
from ...pagesObjects.requestcertpage.requestcertpage import *
from ...pagesObjects.revokecertpage.revokecertpage import *
from ...pagesObjects.serverpage.serverpage import *
from ...pagesObjects.serverpage.createpage import *
from ...pagesObjects.scanpage.scanpage import *
class Utils:
    def __init__(self):
        self.driver = HelperFunc.__init__()
        self.driver.get(url)
        
    def init_database(self,arg):
        HelperFunc.init_results(arg)    

    def login_steps(self):
        
        time.sleep(10)
        lp = LoginPage(self.driver)
        lp.enter_username(username)
        lp.enter_password(password)
        lp.click_login()
        time.sleep(3)
        self.dp = DashbordPage(self.driver)
    
    def tenant_change(self):

        time.sleep(3)
        self.dp.click_dropdown_header()
        time.sleep(3)
        self.dp.click_change_tenant()
        time.sleep(3)
    
    def tenant_delete(self):

        time.sleep(3)
        self.dp.click_delete_tenant()

    def credentials_page(self):

        time.sleep(3)
        self.cp = CredentialPage(self.driver)
        self.cp.click_dropdown_side()
        time.sleep(3)
    
    def create_credential_Microsoft(self):
        
        self.cp.click_add_credential()
        time.sleep(3)
        cc=CreatePage_credentials(self.driver)
        cc.enter_name_credentials()
        cc.pick_authnType_Microsoft()
        cc.click_submit_credentials()
        time.sleep(3)
    
    def create_credential_ejbcace(self):
            
        self.cp.click_add_credential()
        time.sleep(3)
        cc=CreatePage_credentials(self.driver)
        cc.enter_name_credentials()
        cc.pick_authnType_tls_plain_text()
        cc.click_submit_credentials()
        time.sleep(3)
    
    def create_credential_apache97(self):
        
        self.cp.click_add_credential()
        time.sleep(3)
        cc=CreatePage_credentials(self.driver)
        cc.enter_name_credentials()
        cc.pick_authnType_apache97()
        cc.click_submit_credentials()
        time.sleep(3)
    
    def pki_page(self):
            
        time.sleep(3)
        self.pp = PkiPage(self.driver)
        self.pp.click_dropdown_side_pkis()
        self.pp.click_add_pki()
        time.sleep(6)

    def server_page(self):
            
        time.sleep(3)
        self.sp = ServerPage(self.driver)
        self.sp.click_dropdown_side_servers()
        self.sp.click_add_server()
        time.sleep(6)
    
    def create_server_apache97(self):
        
        self.cp=CreatePage_server(self.driver)
        self.cp.enter_name_server()
        self.cp.enter_data_ssh()
        self.cp.pick_credentials()
        self.cp.click_submit_server()
        time.sleep(3)

    def create_pki_Microsoft(self):
        
        self.cp=CreatePage_pki(self.driver)
        self.cp.enter_name_pki()
        self.cp.pick_authnType_Microsoft()
        self.cp.pick_credentials()
        self.cp.click_submit_pki()
        time.sleep(3)
    
    def create_pki_ejbcace(self):
                
        self.cp=CreatePage_pki(self.driver)
        self.cp.enter_name_pki()
        self.cp.pick_authnType_ejbcace()
        self.cp.pick_credentials()
        self.cp.click_submit_pki()
        time.sleep(3)

    def synch_pki(self):
        self.pp.click_sync()
        time.sleep(3)
    
    def usage_page(self):
        time.sleep(3)
        up = UsagePage(self.driver)
        up.click_dropdown_side_usage()
        up.click_add_usage()
        time.sleep(3)
    
    def create_usage_Microsoft(self):
        up = UsagePage(self.driver)
        up.click_add_usage()
        time.sleep(3)
        self.cp=CreatePage_usage(self.driver)
        self.cp.enter_name_usage()
        self.cp.pick_pkiType_Microsoft()
        self.cp.pick_certificate_Authority_Microsoft()
        self.cp.pick_certificate_Profile_Microsoft()
        self.cp.pick_security_Policy_Microsoft()
        self.cp.scroll_by_pressing_down()
        self.cp.pick_Csr_generation_mode()
        self.cp.pick_Default_csr_generation_mode()
        self.cp.scroll_by_pressing_down()
        time.sleep(3)
        self.cp.pick_Certificate_DN_mode()
        self.cp.scroll_by_pressing_down()
        self.cp.pick_key_Algo()
        self.cp.pick_keySize()
        self.cp.click_submit_usage()
        time.sleep(3)

    def create_usage_ejbcace(self):
        up = UsagePage(self.driver)
        up.click_add_usage()
        time.sleep(3)
        self.cp=CreatePage_usage(self.driver)
        self.cp.enter_name_usage()
        self.cp.pick_pkiType_Ejbcace()
        self.cp.pick_End_entity_profile_Ejbcace()
        self.cp.pick_certificate_Authority_Ejbcace()
        self.cp.pick_certificate_Profile_Ejbcace()
        self.cp.pick_security_Policy_Ejbcace()
        self.cp.scroll_by_pressing_down()
        self.cp.pick_Csr_generation_mode()
        self.cp.pick_Default_csr_generation_mode()
        self.cp.scroll_by_pressing_down()
        self.cp.pick_Certificate_DN_mode_2()
        self.cp.scroll_by_pressing_down()
        self.cp.pick_Certificate_SN_mode_2()
        self.cp.scroll_by_pressing_down()
        self.cp.pick_key_Algo()
        self.cp.pick_keySize()
        self.cp.click_submit_usage()
        time.sleep(3)
    
    def request_cert(self):
        time.sleep(3)
        self.rc = RequestCertPage(self.driver)
        self.rc.click_Request_Cert()
        self.rc.pick_usage()
        self.rc.click_submit_RequestCert()
        time.sleep(3)

    def aprove_request_ejb(self):
        self.rc.aprove_request_ejb()
        time.sleep(3)
    
    def aprove_request_Micro(self):
        self.rc.aprove_request_micro()
        time.sleep(3)
        
    def revoke_cert(self):
        
        rc=RevokecertPage(self.driver)
        rc.click_dropdown_side_certificates()
        rc.revoke_cert()
        time.sleep(3)
        rc.click_dropdown_side_revokes()
        rc.approve_revoke()

    def lanuch_scan(self):

        time.sleep(3)
        sc=ScanPage(self.driver)
        sc.click_new_scan()
        time.sleep(3)
        sc.enter_name_scan()
        sc.pick_scan_type()
        sc.pick_scannerServer()
        sc.pick_applicationType()
        sc.click_submit_scan()

    def create_tenant(self):
        time.sleep(3)
        self.dp.click_dropdown_header()
        self.dp.click_create_tenant()
        time.sleep(3)
        