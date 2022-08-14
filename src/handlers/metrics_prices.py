from tornado.web import RequestHandler
from src.services.metrics_prices import MetricsPricesService
from src.views.prices import PricesView


class MetricsPrices(RequestHandler):
    def get(self, metric_id):
        prices_view = PricesView()
        metrics_prices_service = MetricsPricesService(
            self.application.conn)
        prices = metrics_prices_service.fetch_all_by_metric_id_and_dates(
            metric_id)
        prices_output = prices_view.prices_list(prices)
        response = {
            "prices": prices_output
        }
        self.write(response)
