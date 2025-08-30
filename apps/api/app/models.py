from datetime import datetime, date
from typing import Optional
from sqlmodel import SQLModel, Field

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str = Field(index=True, unique=True)
    password_hash: str
    provider: str = "local"
    created_at: datetime = Field(default_factory=datetime.utcnow)

class Organization(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    plan: str = "free"
    created_at: datetime = Field(default_factory=datetime.utcnow)

class OrgMember(SQLModel, table=True):
    org_id: int = Field(foreign_key="organization.id", primary_key=True)
    user_id: int = Field(foreign_key="user.id", primary_key=True)
    role: str = "owner"

class SKU(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    org_id: int = Field(foreign_key="organization.id")
    name: str
    category: str
    fabric: str
    color: str
    motif: str
    price: float

class Sales(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    org_id: int = Field(foreign_key="organization.id")
    sku_id: Optional[int] = Field(default=None, foreign_key="sku.id")
    date: date
    qty: int
    revenue: float
    region: str

class Signal(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    org_id: int = Field(foreign_key="organization.id")
    type: str
    key: str
    value: float
    ts: datetime = Field(default_factory=datetime.utcnow)

class ForecastJob(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    org_id: int = Field(foreign_key="organization.id")
    status: str = "pending"
    horizon_months: int
    created_by: int = Field(foreign_key="user.id")
    created_at: datetime = Field(default_factory=datetime.utcnow)

class ForecastResult(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    job_id: int = Field(foreign_key="forecastjob.id")
    sku_id: Optional[int] = Field(default=None, foreign_key="sku.id")
    date: date
    yhat: float
    yhat_lower: float
    yhat_upper: float
    method: str

class Report(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    org_id: int = Field(foreign_key="organization.id")
    title: str
    params_json: str
    file_path: str
    created_by: int = Field(foreign_key="user.id")
    created_at: datetime = Field(default_factory=datetime.utcnow)

class Subscription(SQLModel, table=True):
    org_id: int = Field(foreign_key="organization.id", primary_key=True)
    provider: str
    status: str
    current_period_end: datetime

class ApiKey(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    org_id: int = Field(foreign_key="organization.id")
    key: str
    name: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
