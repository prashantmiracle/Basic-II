from typing import List


def forecast_trend(data: List[float], steps: int = 1) -> List[float]:
    """Forecast future values using a simple linear trend.

    Parameters
    ----------
    data : list of float
        Historical observations ordered by time.
    steps : int, default 1
        Number of future steps to forecast.

    Returns
    -------
    list of float
        Forecasted values for the specified number of steps.
    """
    if len(data) < 2:
        raise ValueError("Need at least two data points for trend forecasting")

    n = len(data)
    x = list(range(n))
    y = data

    sum_x = sum(x)
    sum_y = sum(y)
    sum_xy = sum(x_i * y_i for x_i, y_i in zip(x, y))
    sum_x2 = sum(x_i * x_i for x_i in x)

    denominator = n * sum_x2 - sum_x ** 2
    if denominator == 0:
        raise ValueError("Cannot compute linear trend")

    slope = (n * sum_xy - sum_x * sum_y) / denominator
    intercept = (sum_y - slope * sum_x) / n

    forecast = []
    for i in range(1, steps + 1):
        x_future = n + i - 1
        y_future = slope * x_future + intercept
        forecast.append(y_future)
    return forecast
