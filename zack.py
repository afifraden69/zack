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
    os.system('python2 zack.py')

#Browser Setting
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('user-agent','Mozilla/5.0 (Linux; Android 6.0.1; SO-04G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.127 Mobile Safari/537.36')]#Change Your Google Chrome User Agent.

#exit#
def exit():
	print "[!] Exit"
	os.sys.exit()

#random#
def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)

#cetak#
def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')

#Text Walking.
def zaki(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)

#But Don't Remove Author Name.
banner = """
╔═╗╔═╗╔═╗╦╔═╦ ╦  ╔═╗╦═╗╔═╗╔═╗╦╔═╔═╗╦═╗
╔═╝╠═╣║  ╠╩╗╚╦╝  ║  ╠╦╝╠═╣║  ╠╩╗║╣ ╠╦╝
╚═╝╩ ╩╚═╝╩ ╩ ╩   ╚═╝╩╚═╩ ╩╚═╝╩ ╩╚═╝╩╚═ \033[1;94m v 1.0
\033[1;34m╔═════════════════════\033[1;96m══════════════════════╗
\033[1;34m║  \033[1;93mAuthor   \033[1;91m: \033[1;92mZacky Tr\033[1;95micker                 \033[1;96m║
\033[1;34m║  \033[1;93mGithub   \033[1;91m: \033[1;92mhttps://\033[1;95mgithub.com/ZAKI-ZK    \033[1;96m║
\033[1;34m║  \033[1;93mFb       \033[1;91m: \033[1;92mfacebook\033[1;95m.com/kang.mazid.9     \033[1;96m║
\033[1;34m╚═════════════════════\033[1;96m══════════════════════╝"""
# titik #
def tik():
	titik = [".   ","..  ","... "]
	for o in titik:
		print("\r[✓] Generating Access Token "+o),;sys.stdout.flush();time.sleep(1)

back = 0
id = []

#user_pass_tools#
def tlogin():
	os.system('clear')
	print banner
	username = raw_input("\033[1;97m[+] Username :\033[1;93m ")
	if username =="zaki":#Free Change.
	    os.system('clear')
	    print banner
	    print "\033[1;92m[✓] Username : "+username+ " (correct)"
	else:
	    print "[!] Invalid Username."
	    time.sleep(0)
	    tlogin()
	    
	passw = raw_input("\033[1;97m[+] Password :\033[1;93m ")
	if passw =="2021":#Free Change.
	    os.system('clear')
	    print banner
	    print "\033[1;92m[✓] Username : " +username+ " (correct)"
	    print "\033[1;92m[✓] Password : " +passw+ "  (correct)"
	    time.sleep(1)
	    zaki ('\033[1;97mPlease Subcribe My Youtube Channel')# Don't Change This.
	    os.system('xdg-open https://youtube.com/channel/UCzL-chxGyjMhrkRPU8dGfMQ')
	    methodlogin()


#Don't Change This.
def methodlogin():
	os.system('clear')
	print banner
	print
	print "\033[1;93m[1] Crack Menu"
	print "[2] Create Access Token (Use Cookie)"
	print ('      ')
	hos = raw_input("\nChoose Option >>  ")
	if hos =="":
		print"[!]  Wrong Input"
		exit()
	elif hos =="1":
	    menu_crack()
	elif hos =="2":
	    cookie()
	else:
	    print "Wrong Input"
	    exit()
	    
#menu_crack#
def menu_crack():
    os.system('clear')
    print banner
    print
    print '\033[1;93m[1] Crack Password sayang,anjing'
    print '[2] Crack Password kontol,ngentod'
    print '[3] Crack Password bangsat,bajingan'
    print '[4] Crack Password doraemon,Spongebob'
    print '[5] Crack Password indonesia,merdeka'
    print '[6] Crack Password nama1,nama12'
    print '[7] Crack Password nama123,nama1234'
    print '[8] Crack Password nama12345,nama123456'
    print '[9] Crack Password 786786,102030'
    print '[10] Crack Password pakistan,karachi'
    print '[11] Crack Password 123456,790790'
    print '[12] Crack Password bangladesh,bengali'
    print '[13] Crack Password name@,name1@'
    print
    pilih_crack()

#Don't Change This.
def pilih_crack():
	msuk = raw_input("\033[1;93mChoose Option >>  ")
	if msuk =="":
		print"\033[1;97m[!]  Wrong Input"
		pilih_crack()
	elif msuk =="1" or msuk =="01":
		os.system('python2 sayang_anjing.py')
	elif msuk =="2" or msuk =="02":
	    os.system('python2 kontol_ngentod.py')
	elif msuk =="3"or msuk =="03":
		os.system('python2 bangsat_bajingan.py')
	elif msuk =="4"or msuk =="04":
		os.system('python2 doraemon_Spongebob.py')
	elif msuk =="5"or msuk =="05":
		os.system('python2 indonesia_merdeka.py')
	elif msuk =="6"or msuk =="06":
		os.system('python2 1_12.py')
	elif msuk =="7"or msuk =="07":
		os.system('python2 123_1234.py')
	elif msuk =="8"or msuk =="08":
		os.system('python2 12345_123456.py')
	elif msuk =="9"or msuk =="09":
		os.system('python2 786786_102030.py')
	elif msuk =="10"or msuk =="10":
		os.system('python2 pakistan,karachi.py')
	elif msuk =="11"or msuk =="11":
		os.system('python2 123456_790790.py')
	elif msuk =="12"or msuk =="12":
		os.system('python2 bangladesh_bengali.py')
	elif msuk =="13"or msuk =="13":
		os.system('python2 @_@.py')
	elif msuk =="0" or msuk =="00":
		pass1()
	else:
		print"\033[1;97m[!]  Wrong Input"
		pilih_crack()
	    
#convert#
def cookie():
	os.system("clear")
	print banner
	print "\033[1;94m[!]use cookies to convert them into tokens"
	cookie = raw_input("\033[1;97m{\033[1;95m?\033[1;97m} Cookie \033[1;91m:\033[1;92m ")
	try:
		data = requests.get('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_', headers = {
		'user-agent'                : 'Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36', # Don't Change This.
		'referer'                   : 'https://m.facebook.com/',
		'host'                      : 'm.facebook.com',
		'origin'                    : 'https://m.facebook.com',
		'upgrade-insecure-requests' : '1',
		'accept-language'           : 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'cache-control'             : 'max-age=0',
		'accept'                    : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
		'content-type'              : 'text/html; charset=utf-8'
		}, cookies = {
		' Cookie '                    : cookie
		})
		find_token = re.search('(EAAA\w+)', data.text)
		hasil    = '\n* Fail : maybe your cookie invalid !!' if (find_token is None) else '\n* Your fb access token : ' + find_token.group(1)
	except requests.exceptions.ConnectionError:
		print "\033[1;97m[\033[1;91m!\033[1;97m] ConnectionError"
	cookie = open("login.txt", 'w')
	cookie.write(find_token.group(1))
	cookie.close()
	print ('\033[1;97m[✓] Access Token Generated Successfully')
	print ("\033[1;94mPlease Wait..")
	time.sleep(2)
	show_token()

#show#
def show_token():
    print "[✓] Your Access Token"
    print "[✓] Copy This Token"
    print(47*"-")
    print
    os.system('cat login.txt')
    print
    print(47*"-")
    raw_input('[Press Enter To Menu Cracking] ')
    menu_crack()
	
if __name__=='__main__':
    methodlogin()
