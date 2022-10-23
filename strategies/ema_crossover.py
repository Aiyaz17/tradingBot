import pandas_ta as ta

def ema_crossover(df):
    # adding emas
    df["EMA_S"] = ta.ema(df.Close, length=8)
    df["EMA_M"] = ta.ema(df.Close, length=20)
    df['ATR']= df.ta.atr()
    df.dropna()


    # ema checks
    emaSignal = 0
    if df['EMA_S'][-1]<df['EMA_M'][-1]:
        emaSignal = 1
    elif df['EMA_S'][-1]>df['EMA_M'][-1]:
        emaSignal = 2

    # crossing ema check
    wicklimit= df.Close[-1]*0.002

    finalSignal = 0
    if emaSignal==1 and df.Open[-1]>df.EMA_S[-1] and df.Close[-1]<df.EMA_S[-1] and df.High[-1]-df.Open[-1]<=wicklimit:
        finalSignal = -1
    if emaSignal==2 and df.Open[-1]<df.EMA_S[-1] and df.Close[-1]>df.EMA_S[-1] and df.Open[-1]-df.Low[-1]<=wicklimit:
        finalSignal = 1

    return finalSignal
