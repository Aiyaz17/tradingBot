import pandas_ta as ta

def bollingerBands(df):
    
    # adding BB
    bbands = ta.bbands(df.close,length=20,std=2)
    bb_df = df.join(bbands)
    bb_df['ATR']= df.ta.atr()
    bb_df.dropna(inplace=True)
    bb_df.reset_index(inplace = True)

    signal = 0
    last = len(bb_df)-1
    if bb_df["close"][last]>bb_df["BBU_20_2.0"][last]:
        signal = -1
    if bb_df["close"][last]<bb_df["BBL_20_2.0"][last]:
        signal = 1
    # Using len() instead of -1 cuz its throwing some error.
    return signal