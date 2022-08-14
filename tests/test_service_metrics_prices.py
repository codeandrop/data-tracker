import pytest
from src.services.metrics_prices import MetricsPricesService


def test_fetch_prices(db_connection, load_prices):
    metrics_prices_service = MetricsPricesService(db_connection)
    all_prices = metrics_prices_service.fetch_all()
    assert len(all_prices) == 9
    assert all_prices[0][1] == 1
    assert all_prices[0][2] == 24480
    assert all_prices[1][1] == 1
    assert all_prices[1][2] == 24490


def test_count_prices(db_connection, load_prices):
    metrics_prices_service = MetricsPricesService(db_connection)
    prices_count = metrics_prices_service.count_records()
    assert prices_count == 9
