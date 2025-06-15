# create_tables.py
from src.models.sinapi_model import Base
from src.db.db_config import engine

def create_tables():
   Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
   create_tables()
   print("Tabelas criadas com sucesso!")
