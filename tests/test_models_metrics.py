import pytest
from src.models.metrics import MetricsModel


def test_update_stdev(db_connection, load_metrics):
    metric = (5, 1)
    metrics_model = MetricsModel(db_connection)
    metrics_model.update_stdev(metric)
    updated_metric = metrics_model.fetch_by_id("1")
    assert updated_metric[4] == 5


def test_update_rank(db_connection, load_metrics):
    metric = (100, 1)
    metrics_model = MetricsModel(db_connection)
    metrics_model.update_rank(metric)
    updated_metric = metrics_model.fetch_by_id("1")
    assert updated_metric[5] == 100
