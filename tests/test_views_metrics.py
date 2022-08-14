import pytest
from src.views.metrics import MetricsView


def test_single_item():
    metric = (1, "KRAKEN", "BTC", "USD", 0, 0)
    metrics_view = MetricsView()
    metric_formatted = metrics_view.metric_item(metric)

    assert metric_formatted["id"] == 1
    assert metric_formatted["market"] == "KRAKEN"
    assert metric_formatted["base"] == "BTC"
    assert metric_formatted["quote"] == "USD"
