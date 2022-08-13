import pytest
from src.models.metrics_prices import MetricsPricesModel


def test_insert_and_fetch_metric(db_connection, load_metrics):
    raw_prices = (
        (1, 2, '2022-08-10 00:00:00', '2022-08-10 00:00:00'),
        (1, 2, '2022-08-10 00:00:00', '2022-08-10 00:00:00'),
        (1, 2, '2022-08-10 00:00:00', '2022-08-10 00:00:00'),
        (1, 2, '2022-08-10 00:00:00', '2022-08-10 00:00:00')
    )
    metrics_prices_model = MetricsPricesModel(db_connection)

    inserted_rows = metrics_prices_model.insert_many(raw_prices)

    assert inserted_rows == 4

    all_rows = metrics_prices_model.fetch_all()

    assert len(all_rows) == 4
