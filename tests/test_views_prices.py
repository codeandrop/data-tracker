import pytest
from src.views.prices import PricesView


def test_prices_view():
    prices = [
        (1, 1, 10, "2022-08-10T02:21:40.955098+00:00",
         "2022-08-10T02:21:40.955098+00:00"),
        (2, 1, 10, "2022-08-10T02:21:40.955098+00:00",
         "2022-08-10T02:21:40.955098+00:00"),
        (3, 1, 10, "2022-08-10T02:21:40.955098+00:00",
         "2022-08-10T02:21:40.955098+00:00"),
    ]

    prices_view = PricesView()
    prices_formatted = prices_view.prices_list(prices)

    for price in prices_formatted:
        assert price["price"] == 10
        assert price["createdAt"] == "2022-08-10T02:21:40.955098+00:00"
