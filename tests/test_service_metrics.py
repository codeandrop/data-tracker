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
    assert all_metrics[0][1] == 'KRAKEN'
    assert all_metrics[0][2] == 'BTC'
    assert all_metrics[0][3] == 'USD'
    assert all_metrics[1][1] == 'KRAKEN'
    assert all_metrics[1][2] == 'ETH'
    assert all_metrics[1][3] == 'USD'


def test_stdev_and_rank_calculation(db_connection, load_prices, update_prices_dates):
    metrics_service = MetricsService(db_connection)
    metrics_service.calculate_and_update_stdev()
    metrics_service.calculate_and_update_rank()
    all_metrics = metrics_service.fetch_all()
    assert len(all_metrics) == 10
    assert all_metrics[0][2] == 'BTC'
    assert all_metrics[0][3] == 'USD'
    assert all_metrics[0][4] == pytest.approx(8.16, 0.1)
    assert all_metrics[0][5] == 1
    assert all_metrics[1][2] == 'ETH'
    assert all_metrics[1][3] == 'USD'
    assert all_metrics[1][4] == pytest.approx(0.81, 0.1)
    assert all_metrics[1][5] == 2
    assert all_metrics[2][2] == 'BNB'
    assert all_metrics[2][3] == 'USD'
    assert all_metrics[2][4] == pytest.approx(0.0, 0.1)
    assert all_metrics[2][5] == 3
