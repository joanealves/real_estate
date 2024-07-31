from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class PropertyBase(BaseModel):
    title: str
    description: Optional[str] = None
    price: float
    location: str

class PropertyCreate(PropertyBase):
    pass

class Property(PropertyBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    name: str
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    properties: List[Property] = []

    class Config:
        orm_mode = True

class ClientBase(BaseModel):
    name: str
    email: str
    phone: str
    address: str

class ClientCreate(ClientBase):
    pass

class Client(ClientBase):
    id: int

    class Config:
        orm_mode = True

class SaleBase(BaseModel):
    property_id: int
    client_id: int
    date: datetime
    value: float
    contract_url: str

class SaleCreate(SaleBase):
    pass

class Sale(SaleBase):
    id: int

    class Config:
        orm_mode = True

class RentBase(BaseModel):
    property_id: int
    client_id: int
    start_date: datetime
    end_date: datetime
    monthly_rent: float
    contract_url: str

class RentCreate(RentBase):
    pass

class Rent(RentBase):
    id: int

    class Config:
        orm_mode = True
