from fastapi import FastAPI
from .db import init_db
from .routers import auth, orgs, ingest, forecast, reports, billing

app = FastAPI(title="Fashion Forecasting API")

init_db()

app.include_router(auth.router)
app.include_router(orgs.router)
app.include_router(ingest.router)
app.include_router(forecast.router)
app.include_router(reports.router)
app.include_router(billing.router)

@app.get("/health")
def health():
    return {"status": "ok"}
