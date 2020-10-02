#!/usr/bin/python

from termcolor import colored
import hashlib

def tryOpen(wordlist):
	global pass_file
	try:
		pass_file = open(wordlist, "r")
	except:
		print("No file at that path")
		quit()

pass_hash = input("Give me the md5 hash value: ")
wordlist = input("Give the path of passcode file: ")
tryOpen(wordlist)

for word in pass_file:
	print(colored("trying: " + word.strip("\n"), 'red'))
enc_wrd = word.encode('utf-8')
md5digest = hashlib.md5(enc_wrd.strip()).hexdigest()

if md5digest == pass_hash:
print(colored("Password found: " + word, 'green'))
exit(0)

print("Passcode is not in the given list")
