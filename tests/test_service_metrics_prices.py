import pytest
from src.services.metrics_prices import MetricsPricesService



def test_fetch_prices(db_connection, load_prices):
    metrics_prices_service = MetricsPricesService(db_connection)
    all_prices = metrics_prices_service.fetch_all()
    assert len(all_prices) == 9
