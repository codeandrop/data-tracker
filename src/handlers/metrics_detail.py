from tornado.web import RequestHandler
from src.services.metrics import MetricsService
from src.views.metrics import MetricsView


class MetricsDetail(RequestHandler):
    def get(self, metric_id):
        metrics_view = MetricsView()
        metrics_service = MetricsService(self.application.conn)
        metric = metrics_service.fetch_by_id(metric_id)
        if metric is None:
            self.set_status(404)
            self.finish({"reason": "Resource not found"})
            return

        metric_output = metrics_view.metric_item(metric)
        response = {
            "metric": metric_output
        }
        self.write(response)
