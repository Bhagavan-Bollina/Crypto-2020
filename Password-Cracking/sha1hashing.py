#!/usr/bin/python

from urllib.request import urlopen
import hashlib

sha1hash = input("[*]Enter the sha1 value[*]: ")
passlist = str(urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt').read(), 'utf-8')

for password in passlist.split('\n'):

hashguess = hashlib.sha1(bytes(password, 'utf-8')).hexdigest()

if hashguess == sha1hash:
print("The password is : " + str(password))
else:
print(Password guess" +str(password) + "does not match, trying the next onr...XD")
print("password is not in list")
