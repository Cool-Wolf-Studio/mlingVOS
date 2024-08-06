#!/usr/bin/env python
# coding=utf-8
# -----------------------------------------------------------------
# By: ling
# date: 2024-07-27
# version = '0.6.2'

#头
import os
import sys
print("Translation is provided by sogou and Google.")
#外处理环
print(os.getcwd())
print(os.listdir())
print(sys.version)
print(sys.platform)
print("Initialization complete!")
fp = os.path.getsize("username.txt")
if fp == 0 :
	#注册(外二)环
	_in = input("What should I call you?")
	_ip = input("Set a secure password!")
	with open('username.txt','w+',encoding="utf-8") as un:
		un.write(str(_in))
	with open('userpassword.txt','w+',encoding='utf-8') as np:
		np.write(str(_ip))
	ieipID = os.getrandom(8)
	ieipE = os.urandom(4)
	ieip = (ieipID + ieipE)
	print("IEIPaddress",ieip)
	ieip = str(ieip)
	with open('ieip.txt','w+',encoding='utf-8') as ieips :
		ieips.write(str(ieip))
	print("IEIP address has been created!")
	print("Welcome new users!")
else:
	un = open("username.txt","r+",encoding="utf-8")
	np = open("userpassword.txt","r+",encoding="utf-8")
	ieips = open("ieip.txt","r+",encoding="utf-8")
	#外运行环
	chenp = np.read()
	cheiip = input("Please input password:")
	while cheiip != chenp :
		cheiip = input("Wrong! Please input password:")
	print("Welcome back.")
#内处理环
import time
import socket
log = "Runing VOS."
lingIP = open("lingIP.txt","r",encoding="utf-8")
#内运行环
print (r'               _ _             ')
print (r'   _ __ ___   | (_)_ __   __ _ ')
print (r"  | '_ ` _ \  | | | '_ \ / _` |")
print (r'  | | | | | | | | | | | | (_| |')
print (r'  |_| |_| |_| |_|_|_| |_|\__, |')
print (r'                         |___/')
print("  ::BASIC github:: v0.6.2-bata1")
#登录环
print("#Time in your area:",time.asctime(time.localtime()))
print("#" * 60)
print("")
#指令堆
inputtext = ""
runcode = "$run"
isw = "welcome new client visit"

while inputtext != "end run" :
	inputtext = input(">>")
	#utc
	if inputtext == "utc" :
		print(time.gmtime())
		chetime = time.gmtime()
		print(time.asctime(chetime))
		log = log + "Query utc."
	
	#日志
	if inputtext == "/what.log" :
		print(log)
		log = log + "Read log."
		
	#当地时
	if inputtext == "time" :
		chetime = time.localtime()
		print(time.asctime(chetime))
		TimeChe = time.localtime
		print(time.strftime('%Y-%m-%d %X (24h)'))
		log = log + "Query time."
		
	#文件管理器-查询源文件夹内容
	if inputtext == "#os.file" :
		print(os.listdir())
		log = log + "Query file."

	#文件管理器-平台名
	if inputtext == "#os.name" :
		print(os.name)
		print(os.uname)
		log = log + "View runtime environment."
		
	#文件管理器-路径
	if inputtext == "#os.sep" :
		print(os.sep,os.altsep,os.curdir,os.pardir,os.extsep,os.pathsep,os.linesep)
		log = log + "View path dividing line rules."
		
	#文件管理器-绝对路径
	if inputtext == "#os.abspath" :
		inputospath = input("File name and suffix>>")
		print(os.path.abspath(inputospath))
		log = log + "The absolute path of"+ inputospath +"has been queried."
		
	#设备-信息
	if inputtext == "VOS" :
		print(os.name,",mlingVOS")
		print("github-basis : noGUI : v0.6.2 : yam version0.0.6")
		print(os.times)
		print()
		log = log + "Query mlingVOS equipment information."
		
	#lingIP
	if inputtext == "lip" :
		print("LingIP:",lingIP.read())
		log = log + "Query your lingIP."
		
	#py版权获取
	if inputtext == "#sys.copy" :
		print(sys.copyright)
		log = log + "Get the open source copyright of person."
		
	#调用sys访问处理的异常情况((三元组))
	if inputtext == "#sys.eio" :
		print(sys.exc_info())
		log = log + "Exc_info."
		
	#修改快捷开服指令
	if inputtext == "/*sk run" :
		print("7082 background manager")
		print("Please don't confuse it with other command names, and you are responsible for any problems.")
		runcode = input("Modify instruction>>")
		log = log + "Set 7082 serve run order."
		
	#yam
	if inputtext == "/*" :
		print("Temporarily closed yam")
		print("#_yam0.0.6/mling/$.yam'bata")
		print("none")
		log = log + "Run yam."
			
	#查询版号变迁
	if inputtext == "/what.v" :
		print("Stand-alone query")
		print("You can query:0.6.2-0.6.0-0.5.23-0.5.21-0.4.18-0.1.0")
		cheVtext = input("Query version>>")
		if cheVtext == "0.6.2" :
			print("Modify the password saving method")
			print("Optimize some important codes.")
		if cheVtext == "0.6.0" :
			print("There is no patch number inherited from the previous version number.")
			print("1.Add command rule(1)")
			print("Add a server that can be used in the LAN. shortcuts/Alterable instruction[$]")
			print("2.New instruction(altogether(Including abandoned)13)")
			print("3.After this version, each version will be equipped with a manual for everyone.")
		if cheVtext == "0.5.23" :
			print("Add naming rules/*Can be understood as higher authority/")
			print("Add shortcut instruction to end running.")
		elif cheVtext == "0.5.21" :
			print("1.Control the instruction rules.")
			print("2.Update input guidance:")
			print("After updating, replace with>>(部分)")
			print("3.Add four new commands")
		elif cheVtext == "0.4.18" :
			print("Add six commands.")
			print("First control rule instruction#")
			print("Start making lip concept and develop it based on IP protocol.")
		elif cheVtext == "0.1.0" :
			print("The number when the project started, there is nothing to introduce.")
		log = log + "Get version."
			
	#结束
	if inputtext == "/*end" :
		print("*")
		inputtext = "end run"
		log = log + "End run."
		
	#测试内容存放
	if inputtext == "/*bata" :
		print("*")
		log = log + "Run bata."
		
	#以本主机v4地址创建服务器,固定端号7082
	if inputtext == runcode :
		print("Creation completed")
		s = socket.socket()         # 创建 socket 对象
		host = socket.gethostname() # 获取本地主机名
		port = 7082                # 设置端口
		s.bind((host, port))        # 绑定端口 
		s.listen(100)                 # 等待客户端连接
		while True:
			c,addr = s.accept()     # 建立客户端连接
			print("connect",addr)
			sti = isw
			if sti != "end" :
				c.send(sti.encode('utf-8'))
				time.sleep(1)
				sti = input("data transmission>> ")
				c.send(sti.encode('utf-8'))
			else :
				c.close()                # 关闭连接
		log = log + "Correct end serve."
				
	#修改7082登录欢迎语
	if inputtext == "/*sk.ww" :
		print("7082 background manager")
		print("We are not responsible for any problems.")
		sti = input("Modify the welcome message(all announcements)->")
		log = log + "Set 7082 welcome word."
		
	#迭代性指令-查询存在的迭代型指令可用代码
	if inputtext == "_@" :
		print("Iterative instruction")
		print("None")
		log = log + "_@"
