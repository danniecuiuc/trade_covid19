from pandas_datareader import data
from pandas import DataFrame

# Banking - quarter report - provision for credit losses and daily return

start_date = '2019-03-01'
end_date = '2020-10-01'

tickers = ['WFC', 'C', 'NTRS', 'STT', 'BK', 'TFC', 'FITB', 'MTB', 'PNC', 'SIVB','RF', 'CFG', 'FRC', 'GS', 'MS', 'BAC', 'JPM']

Data = DataFrame()
for t in tickers:
    mydata = data.DataReader(t, 'yahoo', start_date, end_date)
    mydata['Ticker'] = t
    mydata['Daily Return'] = mydata['Adj Close'].pct_change()
    Data = Data.append(mydata)


# Data = Data[Data.index == '2020-09-30' | Data.index == '2019-03-29']
Data = Data[(Data.index == '2019-03-29') | (Data.index == '2019-06-28') | (Data.index == '2019-09-30') | (Data.index == '2019-12-31')| (Data.index == '2020-03-31') | \
            (Data.index == '2020-06-30') | (Data.index == '2020-09-30')]
Data.to_csv('price.csv')
