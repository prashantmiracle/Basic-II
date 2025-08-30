from fastapi import APIRouter, Depends, UploadFile
from sqlmodel import Session
from .. import models, db, dependencies
import pandas as pd
from io import StringIO

router = APIRouter(prefix="/ingest", tags=["ingest"])

@router.post("/sales")
async def upload_sales(file: UploadFile, session: Session = Depends(db.get_session), user: models.User = Depends(dependencies.get_current_user)):
    content = await file.read()
    df = pd.read_csv(StringIO(content.decode()))
    for _, row in df.iterrows():
        sale = models.Sales(org_id=1, sku_id=None, date=row['date'], qty=int(row['qty']), revenue=float(row['revenue']), region=row['region'])
        session.add(sale)
    session.commit()
    return {"rows": len(df)}
