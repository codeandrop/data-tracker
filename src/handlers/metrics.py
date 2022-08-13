from tornado.web import RequestHandler
from services.metrics import MetricsService
from views.metrics import MetricsView


class Metrics(RequestHandler):
    def get(self):
        metrics_view = MetricsView()
        metrics_service = MetricsService(self.application.conn)
        metrics = metrics_service.fetch_all()
        metrics_output = metrics_view.metrics_list(metrics)
        response = {
            "metrics": metrics_output
        }
        self.write(response)
