from .database import engine
from .models import Base

def setup_database():
    Base.metadata.create_all(engine)
