from bootstrap import Boostrap
from services.metrics_prices import MetricsPricesService
from services.metrics import MetricsService


class PeriodicJobService():
    def __init__(self):
        self.boostrap = Boostrap()

    async def get_prices(self):
        conn = await self.boostrap.create_connection()
        metrics_prices_service = MetricsPricesService(conn)
        metrics_service = MetricsService(conn)
        metrics_prices_service.get_and_store_latest_prices()
        metrics_service.calculate_and_update_stdev()
        metrics_service.calculate_and_update_rank()
        conn.close()
