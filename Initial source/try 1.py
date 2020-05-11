#%%
import random
import csv
import time
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
#%matplotlib tk
plt.style.use('fivethirtyeight')

def animate(i):
    data = pd.read_csv('goog.csv')
    x = data['Time']
    y1 = data['Close']
    y2 = data['Volume']

    plt.cla()
    
    plt.plot(x,y1 , label = "Channel 1")
    plt.plot(x,y2 , label = "Channel 2")

    plt.legend(loc = 'upper right')
    plt.tight_layout()
    
ani = FuncAnimation(plt.gcf(),animate, interval = 2000)
plt.tight_layout()
plt.show()


#%%
x = 0
total1 = 1000
total2 = 2000

fieldnames = ['Date', 'Time','FTP' , 'Open' , 'Close' , 'Volume', 'Bid']

with open('work.csv','w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
    csv_writer.writerheader()
    
while True:
    with open('work.csv', 'a') as csv_file :
        csv_writer = csv.Dicsv_wctWriter(csv_file, fieldnames = fieldnames)
        info = {"x_val" :'Time'
                "total1" : "Close"
                "total2" : "Volume"
                }
        csv_writer.writerow(info)
        print(x_val, total1, total2)
        
    time.sleep(1)
    
    







x = []
y = []

index = count()

    
    
ani = FuncAnimation(plt.gcf(),animate, interval = 2000)
plt.tight_layout()
plt.show()

plt.plot(x, y)


























