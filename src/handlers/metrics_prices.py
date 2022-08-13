from tornado.web import RequestHandler
from services.metrics_prices import MetricsPricesService
from views.prices import PricesView


class MetricsPrices(RequestHandler):
    def get(self, metric_id):
        prices_view = PricesView()
        metrics_prices_service = MetricsPricesService(
            self.application.conn)
        prices = metrics_prices_service.fetch_from_db_by_metric_id(
            metric_id)
        prices_output = prices_view.prices_list(prices)
        response = {
            "prices": prices_output
        }
        self.write(response)
