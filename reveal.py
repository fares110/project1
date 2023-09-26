import requests
from bs4 import BeautifulSoup
import numpy as np
import re

def namemacs(macs):

    lmacs = []
    d = "macs.txt"
    with open(d, 'r') as f:
        for line in f.readlines():
            x = [item.strip() for item in line.split('=')]
            lmacs.append(x)
    #print(lmacs)
    macs = np.array(macs)
    Fmacs =[]
    counter = 0
    macname = np.array(lmacs)
    for i in macs:
        where = np.where(macname == i)
        if where[0].size>0:
            ind = where[0][0]
            e = [str(counter),macname[ind][1], macname[ind][2]]
            Fmacs.append(e)
            counter +=1
        else:
            e = [str(counter),'Unkown Mac', i]
            Fmacs.append(e)
            counter +=1    
    return Fmacs

loginurl = ('http://192.168.1.1/cgi-bin/webproc')
payload = {'getpage': 'html/index.html', 
            'errorpage': 'html/main.html', 
            'var:menu': 'setup',
            'var:page': 'wizard',
            'obj-action': 'auth', 
            ':username': 'admin', 
            ':password': 'admin',
            ':action': 'login',
            ':sessionid': '9138cc7'
    }
hea={
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'ar,en-US;q=0.9,en;q=0.8',
    'Cache-Control':'no-cache',
    'Connection':'keep-alive',
    'Content-Length':'176',
    'Content-Type':'application/x-www-form-urlencoded',
    'Cookie':'sessionid=9138cc7; sessionid=9138cc7; language=en_us; sys_UserName=admin',
    'Host':'192.168.1.1',
    'Origin':'http://192.168.1.1',
    'Pragma':'no-cache',
    'Referer':'http://192.168.1.1/cgi-bin/webproc',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
    }
c= {'cookie':'sessionid=9138cc7; sessionid=9138cc7; language=en_us; sys_UserName=admin'} 

v = requests.post(loginurl, data=payload, headers=hea, allow_redirects=True)
    #print(v)
s = requests.get('http://192.168.1.1/cgi-bin/webproc?getpage=html/index.html&var:menu=status&var:page=wlclients',cookies=c)
    #print(s)
soup = BeautifulSoup(s.text, "html.parser")
scripttags = soup.find_all("script")
f = str(scripttags)
f=f.split("\n")
macs=[]
for i in f:
    if len(i)==29 and i.find('",')>0:
        macs.append(re.sub(',','',i.strip().replace('"','')))
        
