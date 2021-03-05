import requests as r
import json
asset_url='https://849rs099m3.execute-api.ap-southeast-1.amazonaws.com/techtrek/balance'

headers={
    'x-api-key':'rcqYXzQ9PY1rQtUNJB9X56JOvnQWnf27S09nX8Rh',
    'Content-Type': 'application/json',
}

data=json.loads(r.post(history_url,headers=headers).content)

#sorting data
assetSymbol=(data_raw[0]['assetSymbol'])
price_data=[]
time_data=[]
for i in range(0,len(data)):
    price_data.append(data_raw[i]['price'])
    temp=datetime.datetime.fromtimestamp(data_raw[i]['timestamp'])
    time_data.append(temp)
