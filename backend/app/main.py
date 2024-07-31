from fastapi import FastAPI
from app.routes import users, clients, properties, sales, rents  

app = FastAPI()

app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(clients.router, prefix="/clients", tags=["Clients"])
app.include_router(properties.router, prefix="/properties", tags=["Properties"])
app.include_router(sales.router, prefix="/sales", tags=["Sales"])
app.include_router(rents.router, prefix="/rents", tags=["Rents"])  