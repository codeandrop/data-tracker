import os
import sqlite3
from services.metrics_prices import MetricsPricesService


class Boostrap():
    def __init__(self):
        self.conn = None

    async def create_connection(self):
        database_filepath = 'src/data/database.db'

        conn = None
        try:
            conn = sqlite3.connect(os.path.abspath(database_filepath))
        except sqlite3.Error as error:
            print(f"Failed to connect to the database {error}")

        self.conn = conn
        return conn


    async def load_initial_historical_prices(self):
        metrics_prices_service = MetricsPricesService(self.conn)
        historical_data_count = metrics_prices_service.count_records()

        if historical_data_count == 0:
            print("historical data not found on the database, pulling initial data")
            metrics_prices_service.get_prices_from_multiple_metrics()
        else:
            print("historical data found in the database, no need to pull initial data")
