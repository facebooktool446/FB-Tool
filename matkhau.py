import os, sys, re, socket
from time import sleep

red='\u001b[31;1m'
green='\u001b[32;1m'
blue='\u001b[34;1m'
yellow='\u001b[33;1m'
reset='\u001b[0m'

Username = input(green+"Tài Khoản Tool: ")
Password = input(green+"Mật Khẩu Tool: ")

if Username =="facebooktool"and Password=="facebooktool":
	  print(yellow+"Logged in successfully")
	  print (red+"Vui lòng đợi....")
	  sleep(4)
	  os.system('python 123.py')		
else:
	print(red+"Login failed")
	sleep(1)
	os.system('exit')	