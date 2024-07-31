from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
from .. import crud, schemas
from ..database import get_db

router = APIRouter(
    prefix="/properties",
    tags=["Properties"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=schemas.Property)
def create_property(property: schemas.PropertyCreate, db: Session =Depends(get_db)):
    return crud.create_property(db=db, property=property, owner_id=1)

@router.get("/", response_model=List[schemas.Property])
def read_properties(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    properties = crud.get_properties(db, skip=skip, limit=limit)
    return properties

@router.get("/{property_id}", response_model=schemas.Property)
def read_property(property_id: int, db: Session = Depends(get_db)):
    db_property = crud.get_property(db, property_id=property_id)
    if db_property is None:
        raise HTTPException(status_code=404, detail="Property not foound")
    return db_property