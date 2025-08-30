import os
import bcrypt
import jwt
from datetime import datetime, timedelta
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from .. import models, schemas, db

router = APIRouter(prefix="/auth", tags=["auth"])
JWT_SECRET = os.getenv("JWT_SECRET", "secret")

@router.post("/register", response_model=schemas.UserRead)
def register(user: schemas.UserCreate, session: Session = Depends(db.get_session)):
    existing = session.exec(select(models.User).where(models.User.email == user.email)).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email taken")
    hashed = bcrypt.hashpw(user.password.encode(), bcrypt.gensalt()).decode()
    db_user = models.User(email=user.email, password_hash=hashed)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return schemas.UserRead(id=db_user.id, email=db_user.email)

@router.post("/login", response_model=schemas.Token)
def login(user: schemas.UserCreate, session: Session = Depends(db.get_session)):
    db_user = session.exec(select(models.User).where(models.User.email == user.email)).first()
    if not db_user or not bcrypt.checkpw(user.password.encode(), db_user.password_hash.encode()):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    payload = {"sub": str(db_user.id), "exp": datetime.utcnow() + timedelta(hours=12)}
    token = jwt.encode(payload, JWT_SECRET, algorithm="HS256")
    return schemas.Token(access_token=token)
