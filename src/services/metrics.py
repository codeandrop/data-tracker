import math
from src.models.metrics import MetricsModel
from src.services.metrics_prices import MetricsPricesService


class MetricsService():
    def __init__(self, conn):
        self.conn = conn
        self.metrics_model = MetricsModel(self.conn)
        self.metrics_prices_service = MetricsPricesService(
            self.conn)

    def fetch_by_id(self, metric_id):
        return self.metrics_model.fetch_by_id(metric_id)

    def fetch_all(self, options=None):
        return self.metrics_model.fetch_all(options)

    # TODO: Move to helper file
    def calculate_stdev(self, prices):
        if len(prices) == 0:
            return 0

        prices_array = []
        for price in prices:
            prices_array.append(price[2])

        avg_price = sum(prices_array) / len(prices_array)
        deviations = [((p - avg_price)**2) for p in prices_array]
        return math.sqrt(sum(deviations) / len(deviations))

    def calculate_and_update_stdev(self):
        metrics = self.fetch_all()
        for metric in metrics:
            prices = self.metrics_prices_service.fetch_all_by_metric_id_and_dates(
                metric[0])
            stdev = self.calculate_stdev(prices)
            self.metrics_model.update_stdev((stdev, metric[0]))

    def calculate_and_update_rank(self):
        options = {
            "sort": "stdev DESC"
        }
        metrics = self.fetch_all(options=options)
        rank = 1
        for metric in metrics:
            self.metrics_model.update_rank((rank, metric[0]))
            rank += 1
