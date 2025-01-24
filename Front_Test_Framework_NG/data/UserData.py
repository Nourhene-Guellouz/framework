import time
# Description: This file contains the data that is used in the tests



# path to the project (need to be changed to the path of the project on the local machine)

full_path="C:\\Users\\Nourhene\\Downloads\\0202\\Test_Framework\\Front_Test_Framework_NG\\" # must end with "/"

# general data

tenant_name="test_nourhen_auto_"+str(time.time()).replace(".","")       

url="https://test3.digitalberry.fr/"

username="admin@digitalberry.fr"

password="admin"

credential_name="cred_auto_ng"

pki_name="pki_auto_ng"

usage_name="usage_auto_ng"


# credential data Microsoft

microsft_name_cred="microsft_cred"

microsft_username="Administrateur"

microsft_pasword="Test123!!!"

# credential data ejbcace

ejbcace_name_cred="ejbcace_cred"

uploadPrivateKey=full_path+"files/OUTFILE.key"

uploadcertificate=full_path+"files/OUTFILE.crt"

#credential data serever apache97

apache97_name_cred="apache97_cred"

server_username="root"

server_password="joJSaDZbAVC3PmNg"

# pki data Microsoft

microsft_name="microsft_pki_ng"

microsft_fqdn="pki.digitalberry.fr  "

microsft_port="5986"

# pki data ejbcace

ejbcace_name ="ejbcace_pki_ng"

ejbcace_fqdn ="10.30.250.115"

ejbcace_port="15443"

# server data apache97

apache97_name="apache97_pki_ng"

apache97_fqdn="pki.digitalberry.fr  "

apache97_port="5986"