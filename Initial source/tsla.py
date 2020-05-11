from bs4 import BeautifulSoup
import requests as rqs
import time
import csv

#%%
def bois(code):

    URL = "https://in.finance.yahoo.com/quote/"+code
        
    headers = {"user-agent": 'USER_AGENT'}
            
    resp = rqs.get(URL, headers=headers)
            
    soup = BeautifulSoup(resp.text,'html.parser')
        
    array = soup.find(id='quote-header-info').text.split()
        
    for i in array:
        if i=='in':
            stk = (array[(array.index(i)+1)]).split('+')[0][3:]
            
    array = soup.find(id='quote-summary').text.split()
        
    for i in array:
        if 'close' in i:
            stk_close = (array[(array.index(i))])
            stk_close = stk_close.split('close')[1].split('Open')
            stk_open = stk_close
            stk_close = stk_close[0]
            
            stk_open = stk_open[1].split('B')[0]
        
        if 'Volume' in i:
            w1 = (array[(array.index(i))])
            stk_volume = w1.split('Volume')[1].split('Avg')[0]
        
    date = (str(time.localtime().tm_year)+'-'+str(time.localtime().tm_mon)+'-'+str(time.localtime().tm_mday))        
    timen = (str(time.localtime().tm_hour)+':'+str(time.localtime().tm_min)+':'+str(time.localtime().tm_sec))
    al = (stk,stk_open,stk_close,stk_volume,date,timen)
    
    with open('tsla.csv', 'w',newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['LTP','OPEN','CLOSE','VOLUME','DATE','TIME'])
    
    with open('tsla.csv', 'a',newline='') as file:
        writer = csv.writer(file)
        writer.writerow(al)
    
    return al

while True:
    print(bois('TSLA'))
    time.sleep(5)

    
    