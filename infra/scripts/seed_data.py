import random
from datetime import date, timedelta
from sqlmodel import Session
from apps.api.app.db import engine, init_db
from apps.api.app import models


def run():
    init_db()
    with Session(engine) as session:
        org = models.Organization(name="Studio Rama")
        session.add(org)
        session.commit()
        session.refresh(org)
        for i in range(5):
            sku = models.SKU(org_id=org.id, name=f"SKU{i}", category="saree", fabric="cotton", color="red", motif="floral", price=100.0)
            session.add(sku)
            session.commit()
            session.refresh(sku)
            start = date.today() - timedelta(days=730)
            for j in range(24):
                d = start + timedelta(days=30*j)
                sale = models.Sales(org_id=org.id, sku_id=sku.id, date=d, qty=random.randint(1,10), revenue=random.uniform(100,500), region="IN")
                session.add(sale)
        session.commit()

if __name__ == "__main__":
    run()
