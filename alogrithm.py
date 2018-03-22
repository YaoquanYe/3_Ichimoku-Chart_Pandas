from pandas import DataFrame, Series


def HighPriceMax(s, n):
    return Series.rolling(s, n).max()

def LowPriceMin(s, n):
    return Series.rolling(s, n).min()

def PriceAverage(s, n):
    return Series.rolling(s, n).mean()


   
def Ichimoku(H, L, C, t1=9, t2=26, t3=52):
    
    Tenkan_Sen = (HighPriceMax(H, t1) + LowPriceMin(L, t1)) / 2
    Kijun_Sen = (HighPriceMax(H, t2) + LowPriceMin(L, t2)) / 2

    Senkou_Span_A = (Tenkan_Sen + Kijun_Sen) / 2
    Senkou_Span_B = (PriceAverage(H, t3) + PriceAverage(L, t3)) / 2
    
    FrameWork = DataFrame(dict(Tenkan_Sen=Tenkan_Sen, Kijun_Sen=Kijun_Sen,
                               Senkou_Span_A=Senkou_Span_A.shift(t2),
                               Senkou_Span_B=Senkou_Span_B.shift(t2),
                               Chikou_Span=C.shift(-t2)))

    return FrameWork
