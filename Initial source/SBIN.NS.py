#%%
#LIBRARIES
from bs4 import BeautifulSoup
import requests as rqs
import time
import csv

#%%
#Function to get data.

def bois(stk_code):
    URL = "https://in.finance.yahoo.com/quote/"+'SBIN.NS'
    
    headers = {"user-agent": 'USER_AGENT'}
        
    resp = rqs.get(URL, headers=headers)
        
    soup = BeautifulSoup(resp.text,'html.parser')

#FTP    
    array = soup.find(id='quote-header-info').text.split()    
    for i in array:
        if i=='in':
            stk_ftp = (array[(array.index(i)+1)]).split('+')[0].split('-')[0][3:].replace(',','')
            
#CLOSE
    array_2 = soup.find(id='quote-summary').text.split()
    for i in array_2:
        if 'close' in i:
            rw = (array_2[(array_2.index(i))]).split('close')[1].split('Open')
            stk_close = rw[0].replace(',','')

#OPEN,BID            
            rw = rw[1].split('Bid')
            stk_open = rw[0].replace(',','')
            stk_bid = rw[1].replace(',','')

#VOLUME
        if 'Volume' in i:
            rw_2 = (array_2[(array_2.index(i))]).split('Volume')[1].split('Avg')  
            stk_volume = rw_2[0].replace(',','')

#conversion to int
#    stk_ftp = int(stk_ftp)
#    stk_open = int(stk_open)
#    stk_close = int(stk_close)
#    stk_volume = int(stk_volume)
#    stk_bid = int(stk_bid)

#collection    
    date = (str(time.localtime().tm_year)+'-'+str(time.localtime().tm_mon)+'-'+str(time.localtime().tm_mday))        
    timen = (str(time.localtime().tm_hour)+':'+str(time.localtime().tm_min)+':'+str(time.localtime().tm_sec))
    al = (stk_ftp,stk_open,stk_close,stk_volume,stk_bid,date,timen)
    
    return al

#%%
#Packing to csv.

fieldnames = ["Date", "Time", "FTP", "Open", "Close", "Volume", "Bid"]

#headers
with open('sbin.csv', 'a') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()

#loop and write 
while True:
    
    with open('sbin.csv', 'a', newline='') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        now = bois('SBIN.NS')

        info = {
            "Date"  :now[5], 
            "Time"  :now[6], 
            "FTP"   :now[0], 
            "Open"  :now[1], 
            "Close" :now[2], 
            "Volume":now[3], 
            "Bid"   :now[4]
        }

        csv_writer.writerow(info)
        print(info)

    time.sleep(1)