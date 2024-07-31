from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..import models, schemas, crud
from ..database import get_db

router = APIRouter()

@router.post("/rents/", response_model=schemas.Rent)
def create_rent(rent: schemas.RentCreate, db: Session = Depends(get_db)):
    db_rent = models.Rent(**rent.dict())
    db.add(db_rent)
    db.commit()
    db.refresh(db_rent)
    return db_rent

@router.get("/rents/", response_model=List[schemas.Rent])
def read_rents(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    rents = db.query(models.Rent).offset(skip).limit(limit).all()
    return rents

@router.get("/rents/{rent_id}", response_model=schemas.Rent)
def read_rent(rent_id: int, db: Session = Depends(get_db)):
    db_rent = db.query(models.Rent).filter(models.Rent.id == rent_id).first()
    if db_rent is None:
        raise HTTPException(status_code=404, detail="Rent not found")
    return db_rent
