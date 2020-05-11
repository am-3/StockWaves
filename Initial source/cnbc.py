from bs4 import BeautifulSoup
import requests as rqs
import time


def bois(code):
    URL = "https://in.finance.yahoo.com/quote/"+code
    
    headers = {"user-agent": 'USER_AGENT'}
        
    resp = rqs.get(URL, headers=headers)
        
    soup = BeautifulSoup(resp.text,'html.parser')
    
    array = soup.find(id='quote-header-info').text.split()
    
    for i in array:
        if i=='in':
            stk = (array[(array.index(i)+1)]).split('+')[0][3:]
    
    date = (str(time.localtime().tm_year)+'-'+str(time.localtime().tm_mon)+'-'+str(time.localtime().tm_mday))        
    timen = (str(time.localtime().tm_hour)+':'+str(time.localtime().tm_min)+':'+str(time.localtime().tm_sec))
    al = (stk,date,timen)
    
    return al

a = []        


#a += bois('FB'),

while True:
    a += bois('SBIN.NS'),
    time.sleep(10)