#Retrieving data
import requests as r
import json
import datetime
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

history_url = 'https://849rs099m3.execute-api.ap-southeast-1.amazonaws.com/techtrek/pricing/historical'

headers = {
    'x-api-key': 'rcqYXzQ9PY1rQtUNJB9X56JOvnQWnf27S09nX8Rh',
    'Content-Type': 'application/json',
}


data_raw = json.loads(r.post(history_url, headers=headers).content)

#sorting data
assetSymbol=(data_raw[0]['assetSymbol'])
price_data=[]
time_data=[]
for i in range(0,len(data)):
    price_data.append(data_raw[i]['price'])
    temp=datetime.datetime.fromtimestamp(data_raw[i]['timestamp'])
    time_data.append(temp)


#putting into pandas
pd.to_datetime(time_data)
temp_dic={'datetime':time_data,'price':price_data}

df=pd.DataFrame(temp_dic)
#set datetime as index
df=df.set_index('datetime')

#SMA
#Retrieving user input for Simple Moving Average Calc (min, hour days etc.)
minute=0
hour=1
days=0

#Calc cycles
cycles=(days*60+hour)*60+minute

#initialise storage
cleandata_mean_SMA=[]
df['SMA']=df.rolling(window=cycles).mean()

# Plot day and average resampled time series together
fig, full_plot = plt.subplots(figsize=(20,10))
full_plot.plot(df['price'], marker='.', linestyle='-', linewidth=0.5, label=assetSymbol +' Historical Data')
full_plot.plot(df['SMA'], marker='o', markersize=3, linestyle='-', label='Simple Moving Average Resample')
full_plot.set_ylabel('Price')
full_plot.set_xlabel('Time')
title='Digital Asset: ' + assetSymbol
full_plot.set_title(title)
full_plot.legend();
