import os
from fastapi import APIRouter, Depends
from redis import Redis
from rq import Queue
from sqlmodel import Session
from .. import models, db, dependencies, schemas, jobs

redis_conn = Redis.from_url(os.getenv("REDIS_URL", "redis://localhost:6379/0"))
queue = Queue("default", connection=redis_conn)

router = APIRouter(prefix="/forecast", tags=["forecast"])

@router.post("/", response_model=schemas.ForecastStatus)
def create_forecast(req: schemas.ForecastRequest, session: Session = Depends(db.get_session), user: models.User = Depends(dependencies.get_current_user)):
    job = models.ForecastJob(org_id=1, status="queued", horizon_months=req.horizon_months, created_by=user.id)
    session.add(job)
    session.commit()
    session.refresh(job)
    queue.enqueue(jobs.run_forecast, job.id)
    return schemas.ForecastStatus(job_id=job.id, status=job.status)

@router.get("/{job_id}", response_model=schemas.ForecastStatus)
def get_status(job_id: int, session: Session = Depends(db.get_session), user: models.User = Depends(dependencies.get_current_user)):
    job = session.get(models.ForecastJob, job_id)
    return schemas.ForecastStatus(job_id=job.id, status=job.status)
