from sqlalchemy.orm import Session
from . import models, schemas

def get_sales(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Sale).offset(skip).limit(limit).all()

def get_sale(db: Session, sale_id: int):
    return db.query(models.Sale).filter(models.Sale.id == sale_id).first()

def create_sale(db: Session, sale: schemas.SaleCreate):
    db_sale = models.Sale(**sale.dict())
    db.add(db_sale)
    db.commit()
    db.refresh(db_sale)
    return db_sale

def get_rent(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Rent).offset(skip).limit(limit).all()

def get_rent(db: Session, rent_id: int):
    return db.query(models.Rent).filter(models.Rent.id == rent_id).first()

def create_rent(db: Session, rent: schemas.RentCreate):
    print("Rent Data:", rent)
    db_rent = models.Rent(**rent.dict())
    print("DB Rent:", db_rent)
    db.add(db_rent)
    db.commit()
    db.refresh(db_rent)
    print("Final DB Rent", db)
    return db_rent
