#Retrieving data
import requests as r
import json
import datetime
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

asset_url='https://849rs099m3.execute-api.ap-southeast-1.amazonaws.com/techtrek/balance'

headers={
    'x-api-key':'rcqYXzQ9PY1rQtUNJB9X56JOvnQWnf27S09nX8Rh',
    'Content-Type': 'application/json',
}

data_raw=json.loads(r.post(history_url,headers=headers).content)

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
######################Set SMA Cycles here#######################
cycles=1

#initialise storage
cleandata_mean_SMA=[]

cleandata_mean_SMA=df['price'].rolling(window=cycles).mean()

cleandata_mean_SMA
cleandata_mean_SMA.head(50)
