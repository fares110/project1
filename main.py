from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import *
from reveal import *


s= namemacs(macs)
k=''
for x in s:
    k += x[0]+ '->'+ x[1]+ '->'+ x[2]+ '\n'

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self._on_enter_trig = trig = Clock.create_trigger(self._my_on_enter)
        self.bind(on_enter=trig)
    def _my_on_enter(self, *largs):
        self.ids.txt1.text = k 
       
class SecondScreen(Screen):
    pass
class Screens(ScreenManager):
    pass

kv=Builder.load_file('test.kv')

class TestApp(App):
    def build(self):
        
        return kv

if __name__ == '__main__':
    TestApp().run()
























"""import customtkinter
import tkinter
from funcionality import *

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('blue')

app = customtkinter.CTk()

app.title('Control Router')
app.geometry('500x500')

def gg():
    print('gg')

button = customtkinter.CTkButton(master=app, text='get', command = rfile)
button.place(relx=0.5, rely=0.5, anchor= tkinter.CENTER)

app.mainloop()"""



"""from funcionality import *

loginy()
x = getmac()
checkmac(x)

from bs4 import BeautifulSoup
import re
import numpy as np

macname = np.array([[1,'FARES-MOB' , '64:dd:e9:d0:b8:12'],[2,'FARES-PC' , 'd0:37:45:89:48:90'],[3,'SABRINA-MOB' , 'b4:a5:ac:ed:c0:db'],[4,'shaima mob' , 'bc:6a:d1:bf:bd:50'],[5,'sakina mob1' , '3c:19:5e:13:03:31'],[6,'sakina mob2' , 'b8:8f:27:47:bf:bf'],[7,'donia mob' , '9c:f5:31:66:b8:03'],[8,'kenza mob' , 'fc:19:99:5d:04:cb'],[9,'aisa laptop' , '20:16:d8:4b:19:c2']])
loginurl = ('http://192.168.1.1/cgi-bin/webproc')
secureurl = ('http://192.168.1.1/cgi-bin/webproc?getpage=html/index.html&errorpage=html/main.html&var:language=en_us&var:menu=setup&var:page=wizard')

payload = {
    'getpage': 'html/index.html', 
    'errorpage': 'html/main.html', 
    'var:menu': 'setup',
    'var:page': 'wizard',
    'obj-action': 'auth', 
    ':username': 'admin', 
    ':password': 'admin',
    ':action': 'login',
    ':sessionid': '9138cc7'
    }


with HTMLSession() as session:
        session = HTMLSession()
        session.post(loginurl, data=payload)


print(login())

c= {'sessionid':'9138cc7'}    
g1 = session.get('http://192.168.1.1/cgi-bin/webproc?getpage=html/index.html&var:menu=advanced&var:page=wadvance&var:subpage=wlmacfilter', cookies=c)
soup = BeautifulSoup(g1.text, "html.parser")
scripttags = soup.find_all("script")
        
for script in scripttags:
    results = re.search('var G_AllowedMACAddresses="(.*)"', script.text)


        
        
macs = results[1].split(',')

for i in macs:
    where = np.where(macname == i)
    
    if where[0].size>0:
       ind = where[0][0]
       print(macname[ind][1],' = ',macname[ind][2])
    else:
       print('unkown mac = ', i)"""
        