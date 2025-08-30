from typing import Optional, List
from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserRead(BaseModel):
    id: int
    email: EmailStr

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class OrgCreate(BaseModel):
    name: str

class OrgRead(BaseModel):
    id: int
    name: str
    plan: str

class ForecastRequest(BaseModel):
    horizon_months: int

class ForecastStatus(BaseModel):
    job_id: int
    status: str

class ReportCreate(BaseModel):
    title: str
    params: dict

class ReportRead(BaseModel):
    id: int
    title: str
    file_path: str
