import os, sys, re, socket
from time import sleep
from requests import get
import requests
from bs4 import BeautifulSoup
from datetime import datetime
s=0

red='\u001b[31;1m'
green='\u001b[32;1m'
blue='\u001b[34;1m'
yellow='\u001b[33;1m'
reset='\u001b[0m'


os.system('clear')

Username = input(green+"Tài Khoản Tool: ")
Password = input(green+"Mật Khẩu Tool: ")

if Username =="facebooktool"and Password=="facebooktool":
	  print(yellow+"Logged in successfully")
	  print (red+"Vui lòng đợi....")
	  sleep(4)
	  os.system('clear')
	  print(red+'Vui lòng đợi....')
	  print(yellow+"""
		   /$$    /$$$$$$ 
		 /$$$$   /$$$_  $$
		|_  $$  | $$$$\ $$
		  | $$  | $$ $$ $$
		  | $$  | $$\ $$$$
		  | $$  | $$ \ $$$
		 /$$$$$$|  $$$$$$/
		|______/ \______/               
 """)
	  sleep(1)
	  os.system('clear')
	  print(red+'Vui lòng đợi....')                   
	  print(yellow+"""
		  /$$$$$$ 
		 /$$__  $$
		| $$  \ $$
		|  $$$$$$$
		 \____  $$
		 /$$  \ $$
		|  $$$$$$/
		 \______/ 			 
""")  

	  sleep(1)
	  os.system('clear')
	  print(red+'Vui lòng đợi....')
	  print(yellow+"""
		  /$$$$$$ 
		 /$$__  $$
		| $$  \ $$
		|  $$$$$$/
		 >$$__  $$
		| $$  \ $$
		|  $$$$$$/
		 \______/ 
""")
	  sleep(1)
	  os.system('clear')
	  print(red+'Vui lòng đợi....')
	  print(yellow+"""
		 /$$$$$$$$
		|_____ $$/
		     /$$/ 
		    /$$/  
		   /$$/   
		  /$$/    
		 /$$/     
		|__/      
 """)
	  sleep(1)
	  os.system('clear')
	  print(red+'Vui lòng đợi....')
	  print(yellow+"""
		  /$$$$$$ 
		 /$$__  $$
		| $$  \__/
		| $$$$$$$ 
		| $$__  $$
		| $$  \ $$
		|  $$$$$$/
		 \______/ 
 """)
	  sleep(1)
	  os.system('clear')

	  print(red+'Vui lòng đợi....')
	  print(yellow+"""
		 /$$$$$$$ 
		| $$____/ 
		| $$      
		| $$$$$$$ 
		|_____  $$
		 /$$  \ $$
		|  $$$$$$/
		 \______/ 
 """)
	  sleep(1)
	  os.system('clear')

	  print(red+'Vui lòng đợi....')
	  print(yellow+"""
		 /$$   /$$
		| $$  | $$
		| $$  | $$
		| $$$$$$$$
		|_____  $$
		      | $$
		      | $$
		      |__/
""")
	  sleep(1)
	  os.system('clear')

	  print(red+'Vui lòng đợi....')
	  print(yellow+"""
		  /$$$$$$ 
		 /$$__  $$
		|__/  \ $$
		   /$$$$$/
		  |___  $$
		 /$$  \ $$
		|  $$$$$$/
		 \______/ 
""")
	  sleep(1)
	  os.system('clear')

	  print(red+'Vui lòng đợi....')
	  print(yellow+"""
		  /$$$$$$ 
		 /$$__  $$
		|__/  \ $$
		  /$$$$$$/
		 /$$____/ 
		| $$      
		| $$$$$$$$
		|________/
""")
	  sleep(1)
	  os.system('clear')

	  print(red+'Vui lòng đợi....')
	  print(yellow+"""
		   /$$  
		 /$$$$  
		|_  $$  
		  | $$  
		  | $$  
		  | $$  
		 /$$$$$$
		|______/
""")
	  sleep(1)
	  os.system('clear')
	  
	  				
else:
	print(red+"Login failed")
	sleep(1)
	os.system('exit')	




now = datetime.now()
date = now.strftime("%d/%m/%Y")
thoigian = now.strftime("%H:%M:%S")
	
logo1= blue+"""  
   ___            _              _     _____         _ 
  | __|_ _ __ ___| |__  ___  ___| |__ |_   _|__  ___| |
  | _/ _` / _/ -_) '_ \/ _ \/ _ \ / /   | |/ _ \/ _ \ |
  |_|\__,_\__\___|_.__/\___/\___/_\_\   |_|\___/\___/_|
  
  
      \u001b[31;1mCopyright By: Huỳnh Mai Nhật Minh
       \u001b[31;1mYoutube: Nhật Minh Official                                                                           
 """
print(logo1)
sleep(3)

os.system('clear')
print(logo1)

print(green+"Tool Đang Hoạt Động Vào Ngày:",date)
print(green+"Thời Gian Hoạt Động Hiện Tại Lúc:", thoigian)
	
print (yellow+"1.Get Token FB:"+reset)
print (yellow+"2.Tách Token FB:"+reset)
print (yellow+"3.Đăng Nhập Token:"+reset)
print (yellow+"4.Xóa Token Đăng Nhập:"+reset)
print (yellow+"5.Nuôi Facebook:"+reset)

choose = input(blue+'Nhập một số để tiếp tục:')
os.system('clear')
if choose=="1":
	#Tool Get Token
	print(logo1)
	print(yellow+'Nhập Tài Khoản:')
	a = input()
	print(yellow+'Nhập mật khẩu:')
	b = input()
	print('\n')
	c = ('https://b-graph.facebook.com/auth/login?email='+a+'&password='+b+'&access_token=6628568379|c1e620fa708a1d5696fb991c1bde5662&method=post')

	token = get(c).text
	token1 = token
	regex1 = re.compile (r'token":"(.*?)","machine');
	kq = regex1.search (token1)
	print(green+'Token:')
	print (kq.group (1))
	print('\n')
	print("0.Quay Về")
	choose = input(blue+'Nhập 0 để tiếp tục:')
	if choose=='0':
		os.system('python tooltest.py')
		
if choose=='2':
	#Tool Tách Token
	print(logo1)
	print(green+'Nhập Token Cần Tách:')
	token = input()
	regex1 = re.compile (r'token":"(.*?)","machine');
	kq = regex1.search (token)
	print('\n')
	print(red+'Tách Thành Công:')
	print (kq.group (1))
	choose = input(blue+'Nhập 0 để tiếp tục:')
	if choose=='0':
		os.system('python tooltest.py')
		
if choose=='3':
	print(logo1)
	filename ='login.txt'
	f = open (filename, "a")
	print(blue+'Nhập Token Để Đăng Nhập')
	nd_file = input()
	print(red+'Login successfull')
	f.write (nd_file)
	f.close ()
	choose = input(blue+'Nhập 0 để tiếp tục:')
	if choose=='0':
		os.system('python tooltest.py')
		
if choose=='4':
	print(logo1)
	print('Xóa Token Đăng Nhập:\n')
	print('''
Lưu ý bạn phải tạo lại mã Token FB để đăng nhập nếu mã Token đăng nhập của bạn bị xóa
''')

	print("yes")
	print("no")

	a = input('Bạn có muốn tiếp tục xóa : ')

	if a=='yes':	
		os.system('rm -rf login.txt')
		sleep(1)
		print ('Success delete login.txt')
		
		os.system('back')
	if a=='no':
		sleep(1)
		os.system('back')
		
			
if choose=='5':
	print(logo1)
	print(red+''' Lưu ý cần nhập cookie để sử dụng chức năng''')
	cookie=input(blue+"Nhập Cookie FB:"+reset)
while not cookie:
  exit(red+"Không Nhập Cookie Chạy Kiểu Gì Ba!!")
os.system("clear")

print(green+"1.Tự Động Thêm Bạn Bè:"+reset)
print(green+"2.Tự Động Like Bài Viết:"+reset)
print(green+"3.Quay Về:"+reset)
choose=input(blue+"Nhập Một Số Để Chọn Chức Năng:")

url="https://mbasic.facebook.com/friends/center/suggestions/?mff_nav=1&ref=wizard"
url_story="https://mbasic.facebook.com/"
head_fb={
  'Host':'mbasic.facebook.com',
  'user-agent':'Mozilla/5.0 (Linux; Android 10; SM-A505F) AppleWebKit/537.36 (KHTML, like Gecko) coc_coc_browser/89.0.186 Mobile Chrome/83.0.4103.186 Mobile Safari/537.36',
  'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  'accept-language':'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
  'cookie':cookie,
}
	
if choose=="1":
  hl=int(input(blue+"Nhập Delay:"+reset))
  while True:
    web =requests.get(url,headers=head_fb)
    soup=BeautifulSoup(web.text,"html.parser")
    death=soup.title
    for đnp in death.children:
      if "Đăng nhập Facebook" in đnp:
        exit (red+"Die Cookie")
    lo =soup.find_all("a",href=True)
    for t in lo:
      po=t["href"]
      if "/friends/hovercard/mbasic/?" in po:
        web2=requests.get("https://mbasic.facebook.com/"+po,headers=head_fb,allow_redirects=True)
        soup2=BeautifulSoup(web2.text,"html.parser")
        a=soup2.title
        for us in a.children:
          print (us)
        tên=soup2.find_all("a",href=True)
        for i in tên:
          tbb=i["href"]
          if "/a/mobile/friends/add_friend.php?"in tbb:
            requests.get("https://mbasic.facebook.com/"+tbb,headers=head_fb,allow_redirects=True)
            s = s+1
            print (yellow+"[",s,"]","Đã Thêm Bạn Bè")
            for time in range(hl,-1,-1):
              sleep(1)
              print (yellow+"Đợi",time,"Giây",end=" \r")
              
if choose=="2":
  hl=int(input(blue+"Nhập Delay:"+reset))
  while True:
    web3=requests.get(url_story,headers=head_fb)
    soup3=BeautifulSoup(web3.text,"html.parser")
    die=soup3.title
    for đnhap in die.children:
      if "Đăng nhập Facebook" in đnhap:
        exit (red+"Die Cookie")
    tìm=soup3.find_all("a",href=True)
    for story in tìm:
      bài=story["href"]
      if "/story.php?" in bài:
        web4=requests.get("https://mbasic.facebook.com/"+bài,headers=head_fb,allow_redirects=True)
        soup4=BeautifulSoup(web4.text,"html.parser")
        mh =soup4.title
        for ifh in mh.children:
          print ("",end=" \r")
        tìm_a=soup4.find_all("a",href=True)
        for cg in tìm_a:
          link=cg["href"]
          if "/a/like.php?" in link:
            web5=requests.get("https://mbasic.facebook.com/"+link,headers=head_fb,allow_redirects=True)
            s=s+1
            print (green+"[",s,"]","Đã Like Thành Công Bài Viết:",ifh)
            soup5=BeautifulSoup(web5.text,"html.parser")
            block=soup5.title
            for chặn in block.children:
              if "Tài khoản của bạn hiện bị hạn chế"in chặn:
                exit(red+"Bị Block")
            for time in range(hl,-1,-1):
              sleep(1)
              print (yellow+"Đợi",time,"Giây",end=" \r")