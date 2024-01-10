#--> Author's Info
Author    = 'Dapunta Khurayra X'
Facebook  = 'Facebook.com/Dapunta.Khurayra.X'
Instagram = 'Instagram.com/Dapunta.Ratya'
Whatsapp  = '082245780524'
YouTube   = 'Youtube.com/channel/UCZqnZlJ0jfoWSnXrNEj5JHA'

#--> Import Module
import os, sys, bs4, time, datetime, requests, re, random, urllib
from datetime import datetime
from bs4 import BeautifulSoup as bs

#--> Global Variable
bulan = {'1':'Januari','2':'Februari','3':'Maret','4':'April','5':'Mei','6':'Juni','7':'Juli','8':'Agustus','9':'September','10':'Oktober','11':'November','12':'Desember'}
perangkat = '; m_pixel_ratio=1.25; dpr=1.125; wd=360x780'
ok = 0
cp = 0

#--> Warna
P = "\x1b[38;5;231m" # Putih
M = "\x1b[38;5;196m" # Merah
H = "\x1b[38;5;46m"  # Hijau
A = '\x1b[38;5;248m' # Abu-Abu

#--> Clear Terminal
def clear():
    if "linux" in sys.platform.lower():os.system('clear')
    elif "win" in sys.platform.lower():os.system('cls')

#--> Waktu
def waktu():
    _bulan_  = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"][datetime.now().month - 1]
    hari_ini = ("%s%s%s"%(datetime.now().day,_bulan_,datetime.now().year))
    return(str(hari_ini.lower()))

#--> User Agent Vivo
def random_ua_vivo():
    a = random.randrange(110,113)
    b = random.randrange(1000,10000)
    c = random.randrange(10,100)
    os_ver = random.randrange(10,13)                                                            #--> OS Version
    dv_typ = random.choice(['vivo 1951','vivo 1918','V2011A','V2047','V2145','V2227A','V2160']) #--> Device Type
    bl_typ = random.choice(['RP1A','PKQ1','QP1A','TP1A'])                                       #--> Build Type
    dv_ver = random.randrange(100000,250000)                                                    #--> Device Version
    sd_ver = random.randrange(1,10)                                                             #--> Update Version
    ch_ver = f'{a}.0.{b}.{c}'                                                                   #--> Chrome Version
    ua = f'Mozilla/5.0 (Linux; Android {os_ver}; {dv_typ} Build/{bl_typ}.{dv_ver}.00{sd_ver}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch_ver} Mobile Safari/537.36'
    return(ua)

#--> User Agent Samsung
def random_ua_samsung():
    a = random.randrange(110,113)
    b = random.randrange(1000,10000)
    c = random.randrange(10,100)
    os_ver = random.randrange(10,13)                                                            #--> OS Version
    dv_typ = random.choice(['SM-S911B','SM-S908B','SM-G998B','SM-G988B','SM-G973B','SM-N986B']) #--> Device Type
    bl_typ = random.choice(['PPR1','LRX21T','TP1A','RKQ1','SP1A','RP1A'])                       #--> Build Type
    dv_ver = random.randrange(100000,250000)                                                    #--> Device Version
    sd_ver = random.randrange(1,10)                                                             #--> Update Version
    ch_ver = f'{a}.0.{b}.{c}'                                                                   #--> Chrome Version
    ua = f'Mozilla/5.0 (Linux; Android {os_ver}; {dv_typ} Build/{bl_typ}.{dv_ver}.00{sd_ver}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch_ver} Mobile Safari/537.36'
    return(ua)

#--> User Agent Realme
def random_ua_realme():
    a = random.randrange(110,113)
    b = random.randrange(1000,10000)
    c = random.randrange(10,100)
    os_ver = random.randrange(10,13)                                                        #--> OS Version
    dv_typ = random.choice(['RMX3686','RMX3393','RMX3081','RMX2170','RMX2061','RMX2020'])   #--> Device Type
    bl_typ = random.choice(['QP1A','SKQ1','TP1A','RKQ1','SP1A','RP1A'])                     #--> Build Type
    dv_ver = random.randrange(100000,250000)                                                #--> Device Version
    sd_ver = random.randrange(1,10)                                                         #--> Update Version
    ch_ver = f'{a}.0.{b}.{c}'                                                               #--> Chrome Version
    ua = f'Mozilla/5.0 (Linux; Android {os_ver}; {dv_typ} Build/{bl_typ}.{dv_ver}.00{sd_ver}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch_ver} Mobile Safari/537.36'
    return(ua)

#--> User Agent Custom
def random_ua_custom():
    try:
        _file_ = uman
        if 'Android' in str(_file_):
            ad_ver = 'Android ' + str(re.search(r'Android\s+(\d+)', _file_).group(1))
            os_ver = 'Android ' + str(random.randrange(10,13))
            ua1 = _file_.replace(ad_ver,os_ver)
        else: ua1 = _file_
        if 'Build' in str(_file_):
            od_ver = 'Build/' + str(re.search(r'Build/([^;]+)', _file_).group(1))
            bl_typ = random.choice(['QP1A','PPR1','TP1A','RKQ1','SP1A','RP1A','PKQ1'])
            dv_ver = random.randrange(100000,250000)
            sd_ver = random.randrange(1,10)
            nw_str = 'Build/' + str('%s.%s.00%s'%(bl_typ,dv_ver,sd_ver))
            ua2 = ua1.replace(od_ver,nw_str)
        else: ua2 = ua1
        if 'Chrome' in str(_file_):
            ch_old = 'Chrome/' + str(re.search(r'Chrome/([^ ]+)', _file_).group(1))
            a = random.randrange(110,113)
            b = random.randrange(1000,10000)
            c = random.randrange(10,100)
            ch_ver = f'{a}.0.{b}.{c}'
            ch_new = 'Chrome/' + str(ch_ver)
            ua3 = ua2.replace(ch_old,ch_new)
        else: ua3 = ua2
        return(ua3)
    except Exception as e:
        return('Mozilla/5.0 (Linux; Android 12; RMX2170 Build/SKQ1.210216.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.101 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/411.1.0.29.112;]')


#--> Convert Cookies
def cvt(st,ran):
    try:
        if st == 'ok': cookie = ('sb=%s;datr=%s;c_user=%s;xs=%s;fr=%s'%(ran['sb'],ran['datr'],ran['c_user'],ran['xs'],ran['fr']))
        elif st == 'cp': cookie = ('checkpoint=%s;datr=%s;fr=%s'%(ran['checkpoint'],ran['datr'],ran['fr']))
    except Exception as e : cookie = '; '.join([str(x)+"="+str(y) for x,y in ran])
    return(str(cookie))

#--> Logo
def logo():
    print('%s_________                      __        %s________________ %s'%(P,M,P))
    print('%s\_   ___ \_______ ____ _____ _/  |_  ____%s\_   ____|___   \\%s'%(P,M,P))
    print('%s/    \  \/\_  __ \ __ \\\\__  \\\\   __\/ __ \%s|    __)   |  _/%s'%(P,M,P))
    print('%s\ %s0.1 %s\____|  | \/ ___/ / __ \|  | \  ___/%s|   \  |   |   \\%s'%(P,M,P,M,P))
    print('%s \________/|__|  \_____>______/__|  \____>%s|___/  |_______/%s'%(P,M,P))
    print('%s\n      â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€ %sâ€¢ %sRan_Arraya %sâ€¢ %sâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€\n%s'%(A,M,P,M,A,P))

#--> Main Menu
class menu:
    def __init__(self):
        logo()
        self.main_menu()
    def main_menu(self):
        print('%s[%s1%s] %sCreate Account'%(M,P,M,P))
        print('%s[%s2%s] %sCheck Result'%(M,P,M,P))
        print('%s[%s3%s] %sSettings'%(M,P,M,P))
        print('%s[%s4%s] %sBot'%(M,P,M,P))
        x = input(' %sâ””â”€ %sPilih %s: %s'%(M,P,M,P)).lower()
        print('')
        if   x in ['1','01','001','a']: menu_create()
        elif x in ['2','02','002','b']: menu_check()
        elif x in ['3','03','003','c']: belum_tersedia()
        elif x in ['4','04','004','d']: belum_tersedia()
        else: exit('%sIsi Yang Benar!%s'%(M,P))

#--> Menu Create
class menu_create:
    def __init__(self):
        global kelamin, update, tampil, useragent, uman, passtat, password
        try:os.mkdir('Akun_New')
        except Exception as e :pass
        kelamin   = input('%s[%sâ€¢%s] %sAkun Laki/Perempuan/Random [%sl%s/%sp%s/%sr%s] : '%(M,P,M,P,H,P,H,P,M,P)).lower()
        update    = input('%s[%sâ€¢%s] %sAuto Update Info Akun [%sy%s/%st%s] : '%(M,P,M,P,H,P,M,P)).lower()
        tampil    = input('%s[%sâ€¢%s] %sTampilkan Akun CP [%sy%s/%st%s] : '%(M,P,M,P,M,P,H,P)).lower()
        useragent = input('%s[%sâ€¢%s] %sUser Agent Vivo/Samsung/Realme/Manual [v/s/r/m] : '%(M,P,M,P)).lower()
        if useragent in ['m','manual','0','00']:
            uman = input(' %sâ””â”€ %sUser Agent : %s'%(M,P,M))
            if uman == '' or uman == ' ':
                exit('%sIsi Yang Benar!%s'%(M,P))
        else:
            uman = 'Mozilla/5.0 (Linux; Android 12; RMX2170 Build/SKQ1.210216.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.101 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/411.1.0.29.112;]'
        passtat   = input('%s[%sâ€¢%s] %sGunakan Password Random/Manual [%sr%s/%sm%s] : '%(M,P,M,P,H,P,M,P)).lower()
        if passtat in ['m','manual','b','2','02']:
            password = input(' %sâ””â”€ %sPassword : %s'%(M,P,M))
            if len(password) < 6:
                exit('%sPassword Minimal 6 Digit!%s'%(M,P))
            if password in ['akusayangkamu','123456','iloveyou','password','qwerty','sayang','anjing','bismillah']:
                exit('%sGunakan Password Yang Kuat!%s'%(M,P))
        else:
            password = 'dapuntaloverani'
        d = input('%s[%sâ€¢%s] %sBeri Delay (%sDalam Menit%s) : '%(M,P,M,P,M,P))
        if d == '' or d == ' ':
            d = 1
        print('')
        l = int(d)*60
        for y in range(10000):
            create()
            self.hitung(l)
    def hitung(self,a):
        for x in range(a+1):
            print('\r[%sOK:%s%s] [%sCP:%s%s] Tunggu %s Detik         '%(H,str(ok),P,M,str(cp),P,str(a)),end='');sys.stdout.flush()
            a -= 1
            time.sleep(1)

#--> Create Facebook Acc
class create:

    #--> Landing
    def __init__(self):
        self.file  = 'Akun_New/%s.txt'%(waktu())
        self.host  = 'mbasic.facebook.com'
        if   useragent in ['v','vivo','1','01','a']:    ua = random_ua_vivo()
        elif useragent in ['s','samsung','2','02','b']: ua = random_ua_samsung()
        elif useragent in ['r','realme','3','03','c']:  ua = random_ua_realme()
        else : ua  = random_ua_custom()
        self.head1 = {'accept-encoding':'gzip, deflate','accept-language':'en-US,en;q=0.9','cache-control':'max-age=0','referer':f'https://{self.host}/reg/','sec-ch-ua':'','sec-ch-ua-mobile':'?1','sec-ch-ua-platform':'Android','sec-fetch-dest':'document','sec-fetch-mode':'navigate','sec-fetch-site':'same-origin','sec-fetch-user':'?1','upgrade-insecure-requests':'1','user-agent':ua}
        self.r_nm  = requests.Session()
        self.r_fb  = requests.Session()
        self.r_em  = requests.Session()
        self.r_nm.cookies.clear()
        self.r_fb.cookies.clear()
        self.r_em.cookies.clear()
        self.nm, self.gd = self.get_name().split('|')
        self.emfake      = '%s%s@gmail.com'%(self.nm.replace(' ','').lower(),str(random.randrange(1000,10000)))
        self.em          = '%s@jollyfree.com'%(self.nm.replace(' ','').lower())
        self.scrap1()

    #--> Generate Random Name
    def get_name(self):
        if kelamin in ['l','laki','1','01','a']: gder = 'male'
        elif kelamin in ['p','perempuan','2','02','b']: gder = 'female'
        else: gder = random.choice(['male','female'])
        try:
            data = {'country':'indonesian','gender_type':f'{gder}','number_generate':'1','submit':'Generate'}
            reqa = bs(self.r_nm.post('http://ninjaname.net/indonesian_name.php',data=data).content,'html.parser')
            name = re.search('â€¢ (.*?)<br/>',str(reqa)).group(1)
        except Exception as e:
            nam1 = random.choice(['Eka','Dwi','Tri','Budi','Indah','Dewi'])
            nam2 = random.choice(['Nurhayati','Handoko','Setiyani','Susanto','Permata'])
            name = f'{nam1} {nam2}'
        klop = f'{name}|{gder}'
        return(klop)

    #--> Generate Random Phone Number
    def get_nope(self):
        na   = random.choice(['12','22','52'])
        ni   = str(random.randrange(1000,10000))
        nu   = str(random.randrange(1000,10000))
        nope = '+628%s%s%s'%(na,ni,nu)
        return(nope)
    
    #--> Generate Random Password
    def get_pass(self):
        up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        lw = up.lower()
        nb = '0123456789'
        ch = up + lw + nb
        pw = ''.join(random.choice(ch) for _ in range(12))
        return(pw)
    
    #--> Generate Email
    def cek_mail(self):
        time.sleep(15)
        url = f'https://tempmail.email/api/emails?inbox={self.em}'
        req = self.r_em.get(url).json()
        x   = re.search(r'FB-([^ ]+)',str(req)).group(1)
        return(x)

    #--> Scrap Into Login
    def scrap1(self):
        try:
            cid  = str(random.randrange(100,999))
            url1 = f'https://mbasic.facebook.com/reg/?cid={cid}&refsrc=deprecated&_rdr'
            req1 = bs(self.r_fb.get(url1,headers=self.head1).content,'html.parser')
            raq1 = req1.find('form',{'method':'post'})
            if self.gd == 'male': gr = '2'              #--> Laki-Laki
            else: gr = '1'                              #--> Perempuan
            ttl_tgl = str(random.randrange(1,29))       #--> Tanggal Lahir
            ttl_bln = str(random.randrange(1,13))       #--> Bulan Lahir
            ttl_thn = str(random.randrange(1970,2001))  #--> Tahun Lahir
            self.ttl = '%s %s %s'%(ttl_tgl,bulan[ttl_bln],ttl_thn)
            self.nope = self.get_nope()
            if passtat in ['m','b','2','02']: self.pw = password
            else: self.pw = self.get_pass()
            dat = {
                #--> Main Data
                'ns':re.search('name="ns" type="hidden" value="(.*?)"',str(raq1)).group(1),'ccp':re.search('name="ccp" type="hidden" value="(.*?)"',str(raq1)).group(1),'lsd':re.search('name="lsd" type="hidden" value="(.*?)"',str(raq1)).group(1),'jazoest':re.search('name="jazoest" type="hidden" value="(.*?)"',str(raq1)).group(1),'reg_instance':re.search('name="reg_instance" type="hidden" value="(.*?)"',str(raq1)).group(1),'reg_impression_id':re.search('name="reg_impression_id" type="hidden" value="(.*?)"',str(raq1)).group(1),
                #--> Second Data
                'submission_request':'true','helper':'','zero_header_af_client':'','app_id':'','logger_id':'',
                #--> Field Data
                'field_names[]':'firstname','field_names[]':'reg_email__','field_names[]':'sex','field_names[]':'reg_passwd__',
                #--> Input Data
                'firstname':self.nm,'reg_email__':self.nope,'reg_passwd__':self.pw,'pass':self.pw,'sex':gr,'gender':gr,'did_use_age':False,'birthday_day':ttl_tgl,'birthday_month':ttl_bln,'birthday_year':ttl_thn,'is_birthday_confirmed':'confirmed','submit':'Daftar'}
            cok  = '; '.join([str(x)+"="+str(y) for x,y in self.r_fb.cookies.get_dict().items()])
            cok += perangkat
            pos1 = self.r_fb.post(f'https://mbasic.facebook.com/reg/submit/?cid={cid}',headers=self.head1,data=dat,cookies={'cookie':cok})
            pos2 = bs(pos1.content,'html.parser')
            raq2 = pos2.find('form',{'method':'post'})
            if 'checkpoint' in str(raq2['action']):
                self.stat = 'cp'
                self.printin()
            else:
                if 'save-device' in str(pos1.url):
                    print('\rLolos Tahap 1                    ',end='');sys.stdout.flush()
                    self.scrap2(raq2)
        except Exception as e:
            print('\rError Di Scrap 1')
            print(e)
    def scrap2(self,raq1):
        try:
            dat = {'jazoest' : re.search('name="jazoest" type="hidden" value="(.*?)"',str(raq1)).group(1),'fb_dtsg' : re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(raq1)).group(1),'flow' : 'interstitial_nux','next' : False,'nux_source' : 'dbl_nux_after_reg','submit' : 'OK'}
            nek  = 'https://mbasic.facebook.com' + raq1['action']
            cok  = '; '.join([str(x)+"="+str(y) for x,y in self.r_fb.cookies.get_dict().items()])
            cok += perangkat
            pos2 = self.r_fb.post(nek,headers=self.head1,data=dat,cookies={'cookie':cok})
            pos3 = bs(pos2.content,'html.parser')
            print('\rLolos Tahap 2                    ',end='');sys.stdout.flush()
            self.scrap3(pos3,'1')
        except Exception as e:
            print('\rError Di Scrap 2')
            print(e)
    def scrap3(self,pos3,gui):
        try:
            if gui == '1':
                nok = [x['href'] for x in pos3.find_all('a',href=True) if 'changeemail' in str(x['href'])][0]
                nek = 'https://mbasic.facebook.com' + nok
                cok  = '; '.join([str(x)+"="+str(y) for x,y in self.r_fb.cookies.get_dict().items()])
                cok += perangkat
                pes = self.r_fb.get(nek,headers=self.head1,cookies={'cookie':cok})
                pos = bs(pes.content,'html.parser')
                self.scrap3(pos,'2')
            elif gui == '2':
                raq3 = pos3.find('form',{'method':'post'})
                dat = {'fb_dtsg' : re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(raq3)).group(1),'jazoest' : re.search('name="jazoest" type="hidden" value="(.*?)"',str(raq3)).group(1),'next' : False,'old_email' : re.search('name="old_email" type="hidden" value="(.*?)"',str(raq3)).group(1),'reg_instance' : re.search('name="reg_instance" type="hidden" value="(.*?)"',str(raq3)).group(1),'new' : self.emfake,'submit' : 'Add'}
                nek = 'https://mbasic.facebook.com' + raq3['action']
                cok = '; '.join([str(x)+"="+str(y) for x,y in self.r_fb.cookies.get_dict().items()])
                cok += perangkat
                pes = self.r_fb.post(nek,headers=self.head1,data=dat,cookies={'cookie':cok})
                pos = bs(pes.content,'html.parser')
                self.scrap3(pos,'3')
            elif gui == '3':
                nok = [x['href'] for x in pos3.find_all('a',href=True) if 'changeemail' in str(x['href'])][0]
                nek = 'https://mbasic.facebook.com' + nok
                cok  = '; '.join([str(x)+"="+str(y) for x,y in self.r_fb.cookies.get_dict().items()])
                cok += perangkat
                pes = self.r_fb.get(nek,headers=self.head1,cookies={'cookie':cok})
                pos = bs(pes.content,'html.parser')
                self.scrap3(pos,'4')
            elif gui == '4':
                raq3 = pos3.find('form',{'method':'post'})
                dat = {'fb_dtsg' : re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(raq3)).group(1),'jazoest' : re.search('name="jazoest" type="hidden" value="(.*?)"',str(raq3)).group(1),'next' : False,'old_email' : re.search('name="old_email" type="hidden" value="(.*?)"',str(raq3)).group(1),'reg_instance' : re.search('name="reg_instance" type="hidden" value="(.*?)"',str(raq3)).group(1),'new' : self.em,'submit' : 'Add'}
                nek = 'https://mbasic.facebook.com' + raq3['action']
                cok = '; '.join([str(x)+"="+str(y) for x,y in self.r_fb.cookies.get_dict().items()])
                cok += perangkat
                pes = self.r_fb.post(nek,headers=self.head1,data=dat,cookies={'cookie':cok})
                pos = bs(pes.content,'html.parser')
                self.kode = self.cek_mail()
                print('\rLolos Tahap 3                    ',end='');sys.stdout.flush()
                self.scrap4(pos)
        except Exception as e:
            print('\rError Di Scrap 4')
            print(e)
    def scrap4(self,pos4):
        try:
            raq4 = pos4.find('form',{'method':'post'})
            dat = {'fb_dtsg' : re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(raq4)).group(1),'jazoest' : re.search('name="jazoest" type="hidden" value="(.*?)"',str(raq4)).group(1),'c' : self.kode,'submit[confirm]' : 'Confirm'}
            nek  = 'https://mbasic.facebook.com' + raq4['action']
            cok  = '; '.join([str(x)+"="+str(y) for x,y in self.r_fb.cookies.get_dict().items()])
            cok += perangkat
            pos5 = self.r_fb.post(nek,headers=self.head1,data=dat,cookies={'cookie':cok})
            pos6 = bs(pos5.content,'html.parser')
            self.id = self.r_fb.cookies.get_dict()['c_user']
            if 'Telkomsel' in str(pos6):
                print('\rLolos Tahap 4                    ',end='');sys.stdout.flush()
                self.scrap5(pos6)
            else:
                self.stat = 'ok+'
                self.cookie = cvt('ok',self.r_fb.cookies.get_dict())
                self.printin()
        except Exception as e:
            print('\rError Di Scrap 5')
            print(e)
    def scrap5(self,pos5):
        try:
            nok  = [x['href'] for x in pos5.find_all('a',href=True) if 'action=cancel' in str(x['href'])][0]
            nek  = 'https://mbasic.facebook.com' + nok
            cok  = '; '.join([str(x)+"="+str(y) for x,y in self.r_fb.cookies.get_dict().items()])
            cok += perangkat
            pos6 = bs(self.r_fb.get(nek,headers=self.head1,cookies={'cookie':cok}).content,'html.parser')
            raq6 = pos6.find('form',{'method':'post'})
            dat = {'fb_dtsg' : re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(raq6)).group(1),'jazoest' : re.search('name="jazoest" type="hidden" value="(.*?)"',str(raq6)).group(1),'submit'  : 'OK, use data'}
            nuk  = 'https://mbasic.facebook.com' + raq6['action']
            cok  = '; '.join([str(x)+"="+str(y) for x,y in self.r_fb.cookies.get_dict().items()])
            cok += perangkat
            pos7 = self.r_fb.post(nuk,headers=self.head1,data=dat,cookies={'cookie':cok})
            print('\rLolos Tahap 5                    ',end='');sys.stdout.flush()
            self.stat = 'ok+'
            self.cookie = cvt('ok',self.r_fb.cookies.get_dict())
            self.printin()
        except Exception as e:
            print('\rError Di Scrap 6')
            print(e)
    
    #--> Print Result
    def printin(self):
        global cp
        if self.stat == 'cp':
            if tampil in ['t','2','02','b']: pass
            else:
                print('\r%sStatus : %sCheckpoint%s                         '%(P,M,P))
                print('Nama   : %s'%(self.nm))
                print('TTL    : %s'%(self.ttl))
                print('Email  : %s'%(self.nope))
                print('Pass   : %s'%(self.pw))
                print('IP     : %s'%(self.ip('M')))
                print('')
            cp += 1
        elif self.stat == 'ok+':
            self.edit_profil()
        else:
            print('\rStatus : Coba Dulu                         ')
            print('Nama   : %s'%(self.nm))
            print('TTL    : %s'%(self.ttl))
            print('Email  : %s'%(self.em))
            print('Pass   : %s'%(self.pw))
            print('IP     : %s'%(self.ip('M')))
            print('')
    
    #--> Get IP Address
    def ip(self,w):
        try:
            r = requests.Session()
            o = r.get('https://api.ipify.org/?format=json').json()['ip']
            if w == 'H': p = '%s%s%s'%(H,o,P)
            else: p = '%s%s%s'%(M,o,P)
            return(p)
        except Exception as e:
            return('%sUnknown%s'%(M,P))

    #--> Landing Edit Profil
    def edit_profil(self):
        self.xyz = requests.Session()
        if self.gd == 'male':
            self.foto = random.choice(['https://i.pinimg.com/736x/47/cb/b4/47cbb446dd61bfb03308af7dbefdba06.jpg','https://i.pinimg.com/736x/b5/13/22/b51322eeaa2b35fac59444ebde6d8d2f.jpg','https://i.pinimg.com/736x/58/07/ba/5807ba1c263caaa5bbe0639d24ada8e2.jpg','https://i.pinimg.com/736x/72/bd/33/72bd338d114cec8922c14bd98322cf8a.jpg','https://i.pinimg.com/736x/c1/3d/21/c13d2188ceed1679fa2b8963031bc3e6.jpg'])
        else:
            self.foto = random.choice(['https://i.pinimg.com/736x/80/8c/97/808c97eb9c7e017964857b957c125917.jpg','https://i.pinimg.com/736x/f8/a0/da/f8a0da275c48b03550990d3cd27d4eb6.jpg','https://i.pinimg.com/736x/7b/66/55/7b66559151d8c0f50892e27175e5c1d3.jpg','https://i.pinimg.com/736x/6b/00/fe/6b00feaa363d752a4020e55437ba0308.jpg','https://i.pinimg.com/736x/44/b0/7e/44b07e3d57a24bacc0b44b3fb4333908.jpg','https://i.pinimg.com/736x/14/b4/35/14b435422805ff41ecf6688ca67fd132.jpg','https://i.pinimg.com/736x/b6/14/93/b61493683fad328b87b54836226b6eb8.jpg','https://i.pinimg.com/736x/1b/9c/fb/1b9cfbd592dcfc682a14b93698b01e1c.jpg','https://i.pinimg.com/736x/98/ff/d7/98ffd7873189fd7ec7121b4de9cccd09.jpg','https://i.pinimg.com/736x/30/cc/11/30cc11c3453294bca7d657f490e2393a.jpg'])
        if update in ['1','01','y','a']:
            self.profil()
            self.cover()
            self.bio()
            # self.auto_follow()
            # self.kota('https://mbasic.facebook.com/editprofile.php?type=basic&edit=hometown','hometown','hometown[]','Yogyakarta')
            # self.kota('https://mbasic.facebook.com/editprofile.php?type=basic&edit=current_city','current_city','current_city[]','Yogyakarta')
            # self.website()
        self.logout()
    
    #--> Edit Foto Profil
    def profil(self):
        try:
            fot = urllib.request.urlopen(self.foto)
            url = 'https://mbasic.facebook.com/profile_picture/'
            req = bs(self.xyz.get(url,cookies=self.cookie,headers=self.head1).content,'html.parser')
            raq = req.find('form',{'method':'post'})
            dat = {
                'fb_dtsg' : re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(raq)).group(1),
                'jazoest' : re.search('name="jazoest" type="hidden" value="(.*?)"',str(raq)).group(1),
                'submit'  : 'Simpan'}
            fil = {'pic' : fot}
            pos = bs(self.xyz.post(raq['action'],data=dat,files=fil,cookies=self.cookie,headers=self.head1).content,'html.parser')
        except Exception as e:
            pass
    
    #--> Edit Foto Sampul
    def cover(self):
        try:
            fot = urllib.request.urlopen(self.foto)
            url = 'https://mbasic.facebook.com/photos/upload/?cover_photo'
            req = bs(self.xyz.get(url,cookies=self.cookie,headers=self.head1).content,'html.parser')
            raq = req.find('form',{'method':'post'})
            dat = {
                'fb_dtsg'                  : re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(raq)).group(1),
                'jazoest'                  : re.search('name="jazoest" type="hidden" value="(.*?)"',str(raq)).group(1),
                'return_uri'               : re.search('name="return_uri" type="hidden" value="(.*?)"',str(raq)).group(1),
                'return_uri_error'         : re.search('name="return_uri_error" type="hidden" value="(.*?)"',str(raq)).group(1),
                'ref'                      : re.search('name="ref" type="hidden" value="(.*?)"',str(raq)).group(1),
                'csid'                     : re.search('name="csid" type="hidden" value="(.*?)"',str(raq)).group(1),
                'ctype'                    : re.search('name="ctype" type="hidden" value="(.*?)"',str(raq)).group(1),
                'profile_edit_logging_ref' : re.search('name="profile_edit_logging_ref" type="hidden" value="(.*?)"',str(raq)).group(1),
                'submit'                   : 'Unggah'}
            fil = {'file1' : fot}
            pos = bs(self.xyz.post('https://mbasic.facebook.com'+raq['action'],data=dat,files=fil,cookies=self.cookie,headers=self.head1).content,'html.parser')
        except Exception as e:
            pass
    
    #--> Edit Bio
    def bio(self):
        try:
            url = 'https://mbasic.facebook.com/profile/basic/intro/bio/'
            req = bs(self.xyz.get(url,cookies=self.cookie,headers=self.head1).content,'html.parser')
            raq = req.find('form',{'method':'post'})
            dat = {
                'fb_dtsg'         : re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(raq)).group(1),
                'jazoest'         : re.search('name="jazoest" type="hidden" value="(.*?)"',str(raq)).group(1),
                'bio'             : self.nm,
                'publish_to_feed' : True,
                'submit'          : 'Simpan'}
            pos = bs(self.xyz.post('https://mbasic.facebook.com'+raq['action'],data=dat,cookies=self.cookie,headers=self.head1).content,'html.parser')
        except Exception as e:
            pass
    
    #--> Auto Follow
    def auto_follow(self):
        acc = ['1827084332','100000415317575']
        for x in acc:
            url = f'https://mbasic.facebook.com/profile.php?id={x}'
            try:
                req = bs(self.xyz.get(url,cookies=self.cookie,headers=self.head1).content,'html.parser')
                raq = req.find('a',string='Ikuti')
                get = self.xyz.get('https://mbasic.facebook.com'+raq['href'],cookies=self.cookie,headers=self.head1)
            except Exception as e:
                pass
    
    #--> Edit Kota Asal & Tempat Tinggal
    def kota(self,url,a,b,kota):
        try:
            req = bs(self.xyz.get(url,cookies=self.cookie,headers=self.head1).content,'html.parser')
            raq = req.find('form',{'method':'post'})
            dat = {
                'fb_dtsg'    : re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(raq)).group(1),
                'jazoest'    : re.search('name="jazoest" type="hidden" value="(.*?)"',str(raq)).group(1),
                'edit'       : a,
                'type'       : 'basic',
                b : kota,
                'save'       : 'Simpan'}
            pos = bs(self.xyz.post('https://mbasic.facebook.com'+raq['action'],data=dat,cookies=self.cookie,headers=self.head1).content,'html.parser')
        except Exception as e:
            pass
    
    #--> Edit Website
    def website(self):
        try:
            url = 'https://mbasic.facebook.com/editprofile.php?type=contact&edit=website'
            req = bs(self.xyz.get(url,cookies=self.cookie,headers=self.head1).content,'html.parser')
            raq = req.find('form',{'method':'post'})
            dat = {
                'fb_dtsg'    : re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(raq)).group(1),
                'jazoest'    : re.search('name="jazoest" type="hidden" value="(.*?)"',str(raq)).group(1),
                'type'       : 'contact',
                'edit'       : 'website',
                'add_website': '1',
                'new_info'   : 'https://github.com/Dapunta',
                'save'       : 'Tambahkan'}
            pos = bs(self.xyz.post('https://mbasic.facebook.com'+raq['action'],data=dat,cookies=self.cookie,headers=self.head1).content,'html.parser')
        except Exception as e:
            pass
    
    #--> Logout Akun Manual
    def logout(self):
        global ok, cp
        try:
            req = bs(self.xyz.get('https://mbasic.facebook.com/',cookies=self.cookie,headers=self.head1).content,'html.parser')
            url = ['https://mbasic.facebook.com'+x['href'] for x in req.find_all('a',href=True) if 'logout.php' in str(x['href'])][0]
            roq = bs(self.xyz.get(url,cookies=self.cookie,headers=self.head1).content,'html.parser')
            if 'checkpoint' in str(roq):
                if tampil in ['t','2','02','b']: pass
                else:
                    print('\r%sStatus : %sCheckpoint%s                         '%(P,M,P))
                    print('Nama   : %s'%(self.nm))
                    print('TTL    : %s'%(self.ttl))
                    print('Email  : %s'%(self.nope))
                    print('Pass   : %s'%(self.pw))
                    print('IP     : %s'%(self.ip('M')))
                    print('')
                cp += 1
            else:
                print('\r%sStatus : %sOK%s                         '%(P,H,P))
                print('Nama   : %s'%(self.nm))
                print('ID     : %s'%(self.id))
                print('TTL    : %s'%(self.ttl))
                print('Email  : %s'%(self.em))
                print('Pass   : %s'%(self.pw))
                print('IP     : %s'%(self.ip('H')))
                print('Cookie : %s'%(self.cookie))
                print('')
                open(self.file,'a+').write('%s|%s|%s\n'%(self.em,self.pw,self.cookie))
                ok += 1
        except Exception as e:
            if tampil in ['t','2','02','b']: pass
            else:
                print('\r%sStatus : %sCheckpoint%s                         '%(P,M,P))
                print('Nama   : %s'%(self.nm))
                print('TTL    : %s'%(self.ttl))
                print('Email  : %s'%(self.nope))
                print('Pass   : %s'%(self.pw))
                print('IP     : %s'%(self.ip('M')))
                print('')
            cp += 1

#--> Menu Check
class menu_check:

    #--> Tanya Tanya
    def __init__(self):
        self.xyz = requests.Session()
        self.isi = 0
        self.ok  = 0
        self.cp  = 0
        self.head = {'accept-encoding' : 'gzip, deflate','accept-language' : 'en-US,en;q=0.9','cache-control' : 'max-age=0','referer' : 'https://mbasic.facebook.com/login/?next&ref=wizard&fl&login_from_aymh=1&refid=8','sec-ch-ua' : '','sec-ch-ua-mobile' : '?1','sec-ch-ua-platform' : 'Android','sec-fetch-dest' : 'document','sec-fetch-mode' : 'navigate','sec-fetch-site' : 'same-origin','sec-fetch-user' : '?1','upgrade-insecure-requests' : '1','user-agent' : random_ua_vivo()}
        f = 'Akun_New'
        if os.path.isdir(f):
            l = os.listdir(f)
            for y in l:
                c = '%sâ€¢ %s%s'%(M,P,y)
                print(c)
            self.tanya()
        else:
            print('%sMaaf, Belum Ada Hasil %s:(%s\n'%(P,M,P))
    def tanya(self):
        cf = input('%s\n[%sâ€¢%s] %sCek Akun Aktif Dengan Cookie [%sy%s/%st%s] : '%(M,P,M,P,M,P,H,P)).lower()
        if cf in ['y','1','01','a']:
            cok = input('%s[%sâ€¢%s] %sMasukkan Cookie : '%(M,P,M,P))
            try:
                self.token  = self.generate_token(cok)
                self.cookie = {'cookie':cok}
                self.ceker_cookie()
            except Exception as e:
                print('%sCookie Invalid!%s'%(M,P))
                time.sleep(2)
                clear()
                menu()
        else:
            self.ceker_biasa()

    #--> Check Akun Dengan Cookie
    def generate_token(self,cok):
        url = 'https://business.facebook.com/business_locations'
        req = self.xyz.get(url,headers=self.head,cookies={'cookie':cok})
        tok = re.search('(\["EAAG\w+)', req.text).group(1).replace('["','')
        return(tok)
    def ceker_cookie(self):
        try:
            d = input('%s[%sâ€¢%s] %sMasukkan File : '%(M,P,M,P))
            l = 'Akun_New/%s'%(d)
            g = open(l,'r').read().splitlines()
            print('')
            for a in g:
                self.check(a)
            if self.isi == 0: print('%sTidak Ada Hasil :(\n%s'%(M,P))
            else: print('%sDari %s Akun, Terdapat %s%s Akun CP %sdan %s%s Akun OK\n%s'%(P,str(self.isi),M,str(self.cp),P,H,str(self.ok),P))
        except Exception as e:
            print('%sFile Tidak Ditemukan!\n%s'%(M,P))
    def check(self,daf):
        try: 
            em, pw, ck = daf.split('|')
            id = re.search('c_user=(.*?);',str(ck)).group(1)
            url = f'https://mbasic.facebook.com/profile.php?id={id}'
            req = bs(self.xyz.get(url,headers=self.head,cookies=self.cookie).content,'html.parser')
            cek = req.find('title').text
            if cek == 'Konten tidak tersedia' or cek == 'Content unavailable' or cek == 'Kesalahan' :
                print('%sID     : %s%s%s'%(P,M,id,P))
                print('%sEmail  : %s'%(P,em))
                print('%sPass   : %s\n'%(P,pw))
                self.cp += 1
            else:
                print('%sID     : %s%s%s'%(P,H,id,P))
                print('%sEmail  : %s'%(P,em))
                print('%sPass   : %s'%(P,pw))
                print('%sCookie : %s%s%s\n'%(P,H,ck,P))
                self.ok += 1
            self.isi += 1
        except Exception as e: pass

    #--> Check Akun Tanpa Cookie
    def ceker_biasa(self):
        try:
            d = input('%s[%sâ€¢%s] %sMasukkan File : '%(M,P,M,P))
            l = 'Akun_New/%s'%(d)
            g = open(l,'r').read().splitlines()
            print('')
            for a in g: self.lisi(a)
            if self.isi == 0: print('%sTidak Ada Hasil :(\n%s'%(M,P))
            else: print('%sTerdapat %s Akun :)\n%s'%(H,str(self.isi),P))
        except Exception as e:
            print('%sFile Tidak Ditemukan!\n%s'%(M,P))
    def lisi_biasa(self,daf):
        try: 
            em, pw, ck = daf.split('|')
            id = re.search('c_user=(.*?);',str(ck)).group(1)
            print('%sID     : %s%s%s'%(P,H,id,P))
            print('%sEmail  : %s'%(P,em))
            print('%sPass   : %s'%(P,pw))
            print('%sCookie : %s%s%s\n'%(P,H,ck,P))
            self.isi += 1
        except Exception as e: pass

#--> Notice
def belum_tersedia():
    print('%sMaaf, Fitur Ini %sBelum Tersedia%s'%(P,M,P))
    print('%sTunggu Update Selanjutnya...'%(P))
    print('%sTerima Kasih!'%(P))
    print('%s- %sDapunta%s\n'%(P,H,P))

#--> Trigger
if __name__ == '__main__':
    clear()
    menu()
