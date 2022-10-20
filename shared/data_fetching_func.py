import pandas as pd
import datetime as dt

def dynamicDataFetching(fyers,startDate,endDate,symbol,resolution):
    '''
        example - df = dynamicDataFetching(fyers,startDate,endDate,symbol,"1D")
    '''
    # Creating a dataframe to store the data
    df = pd.DataFrame(columns=["date","open","high","low","close","volume"])
    today = dt.date.today()
    range_from=startDate
    while(range_from<=today):
    # Check whether the upcoming endDate is lesser than today if we add 99D or else make it today
        if((range_from + dt.timedelta(days=99))<today):
            range_to = range_from + dt.timedelta(days=99)
        else:
            range_to = today

        # Api call 
        data = {"symbol":symbol,"resolution":resolution,"date_format":"1","range_from":range_from,"range_to":range_to,"cont_flag":"1"}
        res = fyers.history(data)
        res = res["candles"]
        
        # Converting the data into pandas dataframe 
        tempDf = pd.DataFrame(columns=["date","open","high","low","close","volume"])
        for i in range(len(res)):
             tempDf.loc[i]= [
                res[i][0],
                res[i][1],
                res[i][2],
                res[i][3],
                res[i][4],
                res[i][5]]
       
        # Appending the data to the main dataframe
        df = pd.concat([df,tempDf])

        # Updating the range_from to last date of last api call
        range_from=range_to+dt.timedelta(days=1)
    return df

def clean_data(dataframe):
    '''
        example - clean_data(df)
    '''
    # Converting everything to playable format + changing the time zone from utc to ist
    dataframe["date"]= pd.to_datetime(dataframe["date"],unit='s',utc=True).dt.tz_convert('Asia/Kolkata')
    dataframe.set_index("date",inplace=True)
    dataframe["open"]=dataframe["open"].astype(float)
    dataframe["high"]=dataframe["high"].astype(float)
    dataframe["low"]=dataframe["low"].astype(float)
    dataframe["close"]=dataframe["close"].astype(float)
    dataframe["volume"]=dataframe["volume"].astype(float)