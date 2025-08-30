import os
import uuid
from fastapi import APIRouter, Depends
from sqlmodel import Session
from reportlab.pdfgen import canvas
from .. import models, schemas, db, dependencies

router = APIRouter(prefix="/reports", tags=["reports"])
REPORT_DIR = os.path.join(os.getcwd(), "generated_reports")
os.makedirs(REPORT_DIR, exist_ok=True)

@router.post("/", response_model=schemas.ReportRead)
def create_report(req: schemas.ReportCreate, session: Session = Depends(db.get_session), user: models.User = Depends(dependencies.get_current_user)):
    file_name = f"{uuid.uuid4()}.pdf"
    file_path = os.path.join(REPORT_DIR, file_name)
    c = canvas.Canvas(file_path)
    c.drawString(100, 750, req.title)
    c.drawString(100, 730, str(req.params))
    c.save()
    report = models.Report(org_id=1, title=req.title, params_json=str(req.params), file_path=file_path, created_by=user.id)
    session.add(report)
    session.commit()
    session.refresh(report)
    return schemas.ReportRead(id=report.id, title=report.title, file_path=report.file_path)
