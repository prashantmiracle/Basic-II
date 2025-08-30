from sqlmodel import Session
from .db import engine
from .models import ForecastJob, ForecastResult
from .ml.forecast import train_forecast

def run_forecast(job_id: int):
    with Session(engine) as session:
        job = session.get(ForecastJob, job_id)
        if not job:
            return
        job.status = "running"
        session.add(job)
        session.commit()
        results = train_forecast(job.org_id, job.horizon_months)
        for r in results:
            fr = ForecastResult(job_id=job_id, date=r['date'], yhat=r['yhat'], yhat_lower=r['yhat_lower'], yhat_upper=r['yhat_upper'], method='naive')
            session.add(fr)
        job.status = "done"
        session.add(job)
        session.commit()
