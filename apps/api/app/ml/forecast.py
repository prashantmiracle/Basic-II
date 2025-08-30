from datetime import date, timedelta

def train_forecast(org_id: int, horizon: int):
    today = date.today()
    results = []
    for i in range(horizon):
        d = today + timedelta(days=30 * i)
        yhat = 100 + i * 5
        results.append({
            'date': d,
            'yhat': yhat,
            'yhat_lower': yhat * 0.9,
            'yhat_upper': yhat * 1.1
        })
    return results
