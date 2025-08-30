import os
import jwt
from fastapi import Depends, HTTPException, Header
from sqlmodel import Session, select
from . import db, models

JWT_SECRET = os.getenv("JWT_SECRET", "secret")


def get_current_user(authorization: str = Header(...), session: Session = Depends(db.get_session)):
    scheme, _, token = authorization.partition(" ")
    if scheme.lower() != "bearer":
        raise HTTPException(status_code=401, detail="Invalid auth scheme")
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
    user = session.get(models.User, int(payload["sub"]))
    if not user:
        raise HTTPException(status_code=401, detail="User not found")
    return user
