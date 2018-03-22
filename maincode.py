import pandas as pd
import matplotlib.pyplot as plt
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates


def getdata(files, columnname, dates):
    
    #Read data from CSV files
    df_date = pd.DataFrame(index=dates)

    df_value = pd.read_csv(files, index_col='Date',
            parse_dates=True, usecols=['Date', columnname], na_values=['NAN'])
    
    #rename in order to calculate values from different columns
    name = files[:files.find('.')]
    df_value = df_value.rename(columns={columnname: name})
    df = df_date.join(df_value)

    return df


def dateanalysis(time):
    return pd.datetime.strptime(time,"%m/%d/%Y")


def plot(df1, df2, fmt="%m/%d/%Y", title="Ichimoku Chart", x="Date", y="Price"):

    ax = df1.plot(title=title)
    ax.set_xlabel(x)
    ax.set_ylabel(y)

    plt.fill_between(df1.index, df1['Senkou_Span_A'], df1['Senkou_Span_B'],
                     where=df1['Senkou_Span_B'] >= df1['Senkou_Span_A'], facecolor='red', interpolate=True)
    plt.fill_between(df1.index, df1['Senkou_Span_A'], df1['Senkou_Span_B'],
                     where=df1['Senkou_Span_B'] <= df1['Senkou_Span_A'], facecolor='yellow', interpolate=True)
    


    setup = df2.reset_index()[[df2.index.name, "Open", "High", "Low", "Close"]]
    setup[df2.index.name] = setup[df2.index.name].map(mdates.date2num)
    a = candlestick_ohlc(ax, setup.values, width=0.6, colorup='g', alpha = 1)
    
    #set the scales
    ax.xaxis.set_major_formatter(mdates.DateFormatter(fmt))
    ax.autoscale_view()
    ax.xaxis_date()
    ax.grid()
    
    plt.show()

