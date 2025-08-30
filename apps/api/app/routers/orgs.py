from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from .. import models, schemas, db, dependencies

router = APIRouter(prefix="/orgs", tags=["orgs"])

@router.post("/", response_model=schemas.OrgRead)
def create_org(org: schemas.OrgCreate, session: Session = Depends(db.get_session), user: models.User = Depends(dependencies.get_current_user)):
    db_org = models.Organization(name=org.name)
    session.add(db_org)
    session.commit()
    session.refresh(db_org)
    member = models.OrgMember(org_id=db_org.id, user_id=user.id, role="owner")
    session.add(member)
    session.commit()
    return schemas.OrgRead(id=db_org.id, name=db_org.name, plan=db_org.plan)

@router.get("/", response_model=list[schemas.OrgRead])
def list_orgs(session: Session = Depends(db.get_session), user: models.User = Depends(dependencies.get_current_user)):
    org_ids = session.exec(select(models.OrgMember.org_id).where(models.OrgMember.user_id == user.id)).all()
    orgs = session.exec(select(models.Organization).where(models.Organization.id.in_(org_ids))).all()
    return [schemas.OrgRead(id=o.id, name=o.name, plan=o.plan) for o in orgs]
