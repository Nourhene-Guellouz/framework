from .utilitiesTest.utils import *
import sys

args = sys.argv

#to run E2E test for microsoft use: python3 -m Front_Test_Framework_NG.Tests.Main 0
#to run E2E test for ejbcace use: python3 -m Front_Test_Framework_NG.Tests.Main 1

def Main():
    steps = Utils()
    
    #init database
    steps.init_database(args[1])
    
    #login
    steps.login_steps()
    
    #create tenant
    steps.create_tenant()

    
    #change tenant
    steps.tenant_change()
    
    #go to credentials page
    steps.credentials_page()
    
    if(args[1]=='0'):

        #create credential Microsoft
        steps.create_credential_Microsoft()
        
        #go to pki page
        steps.pki_page()
        
        #create pki Microsoft
        steps.create_pki_Microsoft()

        #synch pki synch
        steps.synch_pki()
        
        #go to usage page
        steps.usage_page()

        #create usage Microsoft
        steps.create_usage_Microsoft()
        
        #request cert Microsoft
        steps.request_cert()

        #aprove request
        steps.aprove_request_Micro()
        
        #revoke cert
        steps.revoke_cert()
    elif(args[1]=='1'):
        """
        #create credential ejbcace
        steps.create_credential_ejbcace()
        
        #go to pki page
        steps.pki_page()

        #create pki ejbcace
        steps.create_pki_ejbcace()

        #synch pki synch
        steps.synch_pki()
       
        #go to usage page
        steps.usage_page()

        #create usage ejbcace
        steps.create_usage_ejbcace()
        """
        #request cert Ejbcace
        steps.request_cert()
        
        #aprove request
        steps.aprove_request_Micro()
        
        #revoke cert
        steps.revoke_cert()
    elif(args[1]=='2'):

        #create credential apache97
        steps.create_credential_apache97()

        #go to server page
        steps.server_page()

        #create server apache97
        steps.create_server_apache97()
        time.sleep(30)
        
        #lanuch a scan 
        steps.lanuch_scan()

    #delete tenant
    steps.tenant_delete()

if __name__ == '__main__':
    Main()