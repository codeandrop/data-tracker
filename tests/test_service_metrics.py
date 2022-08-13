import pytest
from src.services.metrics import MetricsService


def test_calculate_stdev_normal_value(db_connection):
    raw_prices = (
        (1, 1, 2, '2022-08-10 00:00:00', '2022-08-10 00:00:00'),
        (2, 1, 2, '2022-08-10 00:00:00', '2022-08-10 00:00:00'),
        (3, 1, 2, '2022-08-10 00:00:00', '2022-08-10 00:00:00'),
        (4, 1, 2, '2022-08-10 00:00:00', '2022-08-10 00:00:00')
    )
    metrics_service = MetricsService(db_connection)

    stdev = metrics_service.calculate_stdev(raw_prices)
    assert stdev == 0.0


def test_fetch_metrics(db_connection, load_metrics):
    metrics_service = MetricsService(db_connection)
    all_metrics = metrics_service.fetch_all()
    assert len(all_metrics) == 10