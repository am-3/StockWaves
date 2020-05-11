from pandas_datareader import data
import matplotlib.pyplot as plt
import pandas as pd
im googlefinance import getQuotes
import json
#
## Define the instruments to download. We would like to see Apple, Microsoft and the S&P500 index.
tickers = ['AAPL', 'MSFT', '^GSPC']
#
## We would like all available data from 01/01/2000 until 12/31/2016.
#start_date = '2010-01-01'
#end_date = '2016-12-31'
#
## User pandas_reader.data.DataReader to load the desired data. As simple as that.
#panel_data = data.DataReader('INPX', 'google', start_date, end_date)

# import stock_info module from yahoo_fin
from yahoo_fin import stock_info as si
#Then, obtaining the current price of a stock is as simple as one line of code:

## get live price of Apple
#print('aaple:',si.get_live_price("aapl"))
# 
## or Amazon
#print('amazon',si.get_live_price("amzn"))
# 
## or any other ticker
#for ticker in tickers:
#    print(ticker,si.get_live_price(ticker))
#
#hist = []
while True:
    dr = si.get_live_price('tsla')
    hist += [dr]
    print('TM',dr)

print (json.dumps(getQuotes('AAPL'), indent=2))
