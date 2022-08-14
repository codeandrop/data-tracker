import asyncio
from tornado.ioloop import PeriodicCallback
from tornado.web import Application
from tornado.options import define, options
from src.bootstrap import Boostrap
from src.handlers.main_handler import MainHandler
from src.handlers.metrics import Metrics
from src.handlers.metrics_detail import MetricsDetail
from src.handlers.metrics_prices import MetricsPrices
from src.services.periodic_job import PeriodicJobService

define("port", default=8888, help="run on the given port", type=int)


class BaseApplication(Application):
    def __init__(self, conn):
        self.conn = conn
        handlers = [
            (r"/", MainHandler),
            (r"/metrics", Metrics),
            (r"/metrics/([^/]+)", MetricsDetail),
            (r"/metrics/([^/]+)/prices", MetricsPrices),
        ]
        super().__init__(handlers)


async def scheduler():
    print("get latest prices, update stdev, and update ranks")
    periodic_job_service = PeriodicJobService()
    await periodic_job_service.get_prices()


async def main():
    boostrap = Boostrap()
    conn = await boostrap.create_connection()
    await boostrap.load_initial_historical_prices()
    app = BaseApplication(conn)
    app.listen(options.port)
    print(f"Server running on http://localhost:{options.port}")

    # TODO: move miliseconds to config file
    period_callback = PeriodicCallback(scheduler, 60000)
    period_callback.start()

    await asyncio.Event().wait()
