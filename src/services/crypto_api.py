from datetime import datetime, timedelta
import time
import configparser
import requests


class CryptoApi():
    def __init__(self):
        self.base_url = "https://api.cryptowat.ch"

        config = configparser.ConfigParser()
        config.read('./src/config.ini')

        self.period = int(config['CRYPTO_API']['Period'])
        self.historical_window = int(
            config['CRYPTO_API']['HistoricalWindowDay'])

    def get_historical_prices(self, options):
        now = datetime.now()
        end_date = int(time.mktime(now.timetuple()))
        delta_date = now - timedelta(days=self.historical_window)
        start_date = int(time.mktime(delta_date.timetuple()))

        request_url = f"{self.base_url}/markets/{options['market']}/{options['base']}{options['quote']}/ohlc?period={self.period}&after={start_date}&before={end_date}"
        response = requests.get(request_url)
        return response.json()

    def get_latest_price(self, options):
        request_url = f"{self.base_url}/markets/{options['market']}/{options['base']}{options['quote']}/price"
        response = requests.get(request_url)
        return response.json()
