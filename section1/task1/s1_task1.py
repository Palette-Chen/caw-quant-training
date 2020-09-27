import requests
import time
import datetime
import numpy as np
import pandas as pd

start_date = '2017/04/01'
end_date = '2020/04/01'
start_timestamp = datetime.datetime.strptime(start_date, "%Y/%m/%d").timestamp()
end_timestamp = datetime.datetime.strptime(end_date, "%Y/%m/%d").timestamp() + 3600 * 23

timeTo = end_timestamp
data = []
while timeTo > start_timestamp:
    payload = {'fsym':'BTC', 'tsym':'USDT', 'toTs':timeTo, 'e':'binance', 'limit':2000}
    r = requests.get('https://min-api.cryptocompare.com/data/v2/histohour', params = payload)
    content = r.json()
    timeFrom = content['Data']['TimeFrom']
    timeTo = timeFrom - 3600
    current_data = content['Data']['Data']
    data = current_data + data

df = pd.DataFrame(data)
df = df[df['time'] >= start_timestamp]

def toUnixTime(t):
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(t))

df['time'] = df['time'].apply(toUnixTime)

df = df[['close', 'high', 'low', 'open', 'volumefrom', 'volumeto', 'time']]
df.columns = ['close', 'high', 'low', 'open', 'volume', 'baseVolume', 'datetime']

df.to_csv(r'/Users/thi/Desktop/caw-quant-training/section1/task1/BTC_USDT_1h_Palette.csv', index = False)


