import pytest
from forecast import forecast_trend


def test_linear_trend():
    data = [1, 2, 3, 4, 5]
    result = forecast_trend(data, steps=2)
    assert result == pytest.approx([6.0, 7.0])


def test_custom_slope():
    data = [2, 4, 6, 8]
    result = forecast_trend(data, steps=1)
    assert result == pytest.approx([10.0])
