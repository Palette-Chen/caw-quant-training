import requests
import time
import datetime
import pandas as pd

class API_hour:

    url = 'https://min-api.cryptocompare.com/data/v2/histohour'
    
    def __init__(self, fsym, tsym, start_date, end_date, e):
        self.fsym = fsym
        self.tsym = tsym
        self.start_date = start_date
        self.end_date = end_date
        self.e = e

        start_timestamp = self.to_UnixTime(self.start_date)
        end_timestamp = self.to_UnixTime(self.end_date) + 3600 * 23

        timeTo = end_timestamp
        data = []

        while timeTo > start_timestamp:
            payload = {'fsym': self.fsym, 'tsym': self.tsym, 'toTs': timeTo, 'e': self.e, 'limit': 2000}
            r = self.get_URL(API_hour.url, payload)
            content = r.json()
            timeFrom = content['Data']['TimeFrom']
            timeTo = timeFrom - 3600
            current_data = content['Data']['Data']
            data = current_data + data

        df = pd.DataFrame(data)
        df = df[df['time'] >= start_timestamp]

        df['time'] = df['time'].apply(self.to_UTC)

        df = df[['close', 'high', 'low', 'open', 'volumefrom', 'volumeto', 'time']]
        df.columns = ['close', 'high', 'low', 'open', 'volume', 'baseVolume', 'datetime']

        df.to_csv('./section1/task1/BTC_USDT_1h_Palette_optional_1.csv', index=False)

    def to_UnixTime(self, date):
        return datetime.datetime.strptime(date, "%Y/%m/%d").timestamp()

    def to_UTC(self, timestamp):
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timestamp))

    def get_URL(self, url, parameter):
        return requests.get(url, params=parameter)


API_hour('BTC', 'USDT', '2017/04/01', '2020/04/01', 'binance')


class API_mktcapfull:

    url = 'https://min-api.cryptocompare.com/data/top/mktcapfull'

    def __init__(self, tsym):
        self.tsym = tsym

        data_list = []
        data = []
        page = 0
        
        try:
            while page < 1000:
                payload = {'tsym': self.tsym, 'limit': 100, 'page': page}
                r = self.get_URL(API_mktcapfull.url, payload)
                content = r.json()
                current_data_list = content['Data']
                data_list = data_list + current_data_list
                page += 1
        except:
            TypeError
            
        for item in data_list:
            data.append(item['CoinInfo'])

        df = pd.DataFrame(data)
        df = df[['Id', 'Name', 'FullName']]

        df.to_csv('./section1/task1/BTC_USDT_1h_Palette_optional_2.csv', index=False)   

    def get_URL(self, url, parameter):
        return requests.get(url, params=parameter)


API_mktcapfull('USD')


    










