from pandas_datareader import data as pdr
import matplotlib.pyplot as plt
import numpy as np
stock_ticker = 'PCG'
start_date = '2009-01-01'
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

money = 25000.
starting_value = opening[-1]
stocks = 0
init_value = 25000.
value_list = []
stocks_list = []
for day in trading_days:
    day = int(day)
    if (opening[day] < opening[day - 1]) and (money > opening[day]):
        stocks += 1
        money -= opening[day]
        value = money + stocks*opening[day]
        value_list.append(value/1000.)
        stocks_list.append(stocks)
    elif (opening[day] > opening[day - 1]) and (stocks > 0.0):
        stocks -= 1
        money += opening[day]
        value = money + stocks*opening[day]
        value_list.append(value/1000.)
        stocks_list.append(stocks)
        
plt.plot(value_list)
plt.plot(stocks_list)
plt.show()
