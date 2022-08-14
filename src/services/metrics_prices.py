from datetime import datetime, timedelta
import pytz
import configparser
from src.models.metrics import MetricsModel
from src.models.metrics_prices import MetricsPricesModel
from src.services.crypto_api import CryptoApi


class MetricsPricesService():
    def __init__(self, conn):
        self.conn = conn
        self.metrics_model = MetricsModel(self.conn)
        self.metrics_prices_model = MetricsPricesModel(self.conn)

        config = configparser.ConfigParser()
        config.read('./src/config.ini')

        self.period = int(
            config['CRYPTO_API']['Period'])
        self.historical_window_seconds = int(
            config['DEFAULT']['HistoricalDataWindowMS'])
        self.crypto_api = CryptoApi()

    def count_records(self):
        return self.metrics_prices_model.count_records()

    def fetch_all(self):
        return self.metrics_prices_model.fetch_all()

    def fetch_all_by_metric_id_and_dates(self, metric_id):
        now = datetime.now()
        end_date = now.isoformat()
        delta_date = now - timedelta(seconds=self.historical_window_seconds)
        start_date = delta_date.isoformat()
        return self.metrics_prices_model.fetch_all_by_metric_id_and_dates(metric_id, start_date, end_date)

    def insert(self, record):
        return self.metrics_prices_model.insert(record)

    def insert_many(self, rows):
        return self.metrics_prices_model.insert_many(rows)

    def prepare_data_to_insert(self, metric_id, prices):
        rows = prices['result'][self.period]
        filtered_information = []
        time_zone = pytz.utc
        for row in rows:
            iso_date = datetime.fromtimestamp(row[0], time_zone).isoformat()
            filtered_information.append(
                [metric_id, row[4], iso_date, iso_date])

        return filtered_information

    def get_prices_from_multiple_metrics(self):
        metrics = self.metrics_model.fetch_all()
        for metric in metrics:
            options = {
                "market": metric[1],
                "base": metric[2],
                "quote": metric[3]
            }
            historical_prices = self.crypto_api.get_historical_prices(
                options)
            filtered_information = self.prepare_data_to_insert(
                metric[0], historical_prices)
            inserted_rows = self.insert_many(filtered_information)
            print(f"{inserted_rows} records inserted.")

    def prepare_latest_data_to_insert(self, metric, price):
        now = datetime.now()
        now_utc = now.astimezone(pytz.utc).isoformat()
        latest_price = price['result']['price']
        return (metric[0], latest_price, now_utc, now_utc)

    def get_and_store_latest_prices(self):
        metrics = self.metrics_model.fetch_all()
        for metric in metrics:
            options = {
                "market": metric[1],
                "base": metric[2],
                "quote": metric[3]
            }

            price = self.crypto_api.get_latest_price(
                options)

            record = self.prepare_latest_data_to_insert(metric, price)
            self.insert(record)
