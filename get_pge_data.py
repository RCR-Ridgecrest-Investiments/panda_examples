from pandas_datareader import data as pdr
import matplotlib.pyplot as plt
import numpy as np
stock_ticker = 'PCG'
start_date = '2017-01-01'
stop_date = '2018-12-24'
data = pdr.get_data_yahoo(stock_ticker, start_date, stop_date) # the data comes in a panda array type with timestamps and labels
np_array_stock_data = data.values # this strips it to a array without timestamps and six columns
highs = np_array_stock_data[:,0]
lows = np_array_stock_data[:,1]
opening = np_array_stock_data[:,2]
closing = np_array_stock_data[:,3]
volume = np_array_stock_data[:,4]
adj_close = np_array_stock_data[:,5]
trading_days = np.linspace(0, len(highs) -1, len(highs))
fig, (ax1, ax2)  = plt.subplots(2, 1, sharex=True)
ax1.plot(trading_days, opening, label = 'Open value')
ax1.plot(trading_days, closing, label = 'Close value')
ax1.plot(trading_days, highs, label = 'Day high')
ax1.plot(trading_days, lows, label = 'Day low')
ax1.set_ylabel('Dollers')
ax2.bar(trading_days, volume/1e6)
ax2.set_ylabel('Millions of shares')
ax1.legend()
ax2.set_xlabel('Trading days since '+ start_date)
fig.suptitle(stock_ticker, fontsize=16)
plt.show()
