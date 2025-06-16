from src.db.connection import engine
from src.models.sinapi_model import Base

def init_db():
   Base.metadata.create_all(bind=engine)
