from pandas_datareader import data as pdr
stock_ticker = 'PCG'
start_date = '2009-01-01'
stop_date = '2017-10-01'
data = pdr.get_data_yahoo(stock_ticker, start_date, stop_date)
print data
