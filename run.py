import pandas as pd
from alogrithm import *
from maincode import *

def run():
    
    date_start = '2009-11-01'
    date_end = '2010-08-01'
    
    column_name = ['High', 'Low', 'Close']
    DataFrameList = []

    for name in column_name:
        df = getdata('SPLS.csv', name, pd.date_range(date_start, date_end))
        DataFrameList.append(df)
 
    df_High = DataFrameList[0]['SPLS'].dropna()
    df_Low = DataFrameList[1]['SPLS'].dropna()
    df_Close = DataFrameList[2]['SPLS'].dropna()
    
    dfCandlestick = pd.read_csv("SPLS.csv", parse_dates=['Date'], date_parser=dateanalysis)
    # Set the Date as label 
    dfCandlestick = dfCandlestick.set_index('Date')

    plot(Ichimoku(df_High, df_Low, df_Close), dfCandlestick)


if __name__ == "__main__":
    run()