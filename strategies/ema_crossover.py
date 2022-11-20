import pandas_ta as ta

def ema_crossover(df):
    # adding emas
    df["EMA_S"] = ta.ema(df.close, length=8)
    df["EMA_M"] = ta.ema(df.close, length=20)
    df['ATR']= df.ta.atr()
    df=df.dropna()

    # ema checks
    emaSignal = 0
    if (df['EMA_S'][-1]<df['EMA_M'][-1]) & ( df['EMA_S'][-2]>df['EMA_M'][-2]):
        emaSignal = -1
    elif (df['EMA_S'][-1]>df['EMA_M'][-1]) & (df['EMA_S'][-2]<df['EMA_M'][-2]):
        emaSignal = 1

    ## crossing ema check
    # wicklimit= df.close[-1]*0.2

    # finalSignal = 0
    # if emaSignal==-1 and df.open[-1]>df.EMA_S[-1] and df.close[-1]<df.EMA_S[-1] and df.high[-1]-df.open[-1]<=wicklimit:
    #     finalSignal = -1
    # if emaSignal==1 and df.open[-1]<df.EMA_S[-1] and df.close[-1]>df.EMA_S[-1] and df.open[-1]-df.low[-1]<=wicklimit:
    #     finalSignal = 1

    return emaSignal
