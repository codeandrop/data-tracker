
from datetime import datetime, timedelta
import time
import requests

# TODO: call config file and default values


class CryptoApi():
    def __init__(self):
        self.base_url = "https://api.cryptowat.ch"
        self.period = 60  # TODO: update from config
        # TODO: convert to seconds
        self.historical_window = 1  # 1 day TODO: update from config

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
