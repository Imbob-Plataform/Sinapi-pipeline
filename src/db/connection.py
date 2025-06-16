# src/db/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.db.credentials import credenciais
from urllib.parse import quote_plus

password = quote_plus(credenciais['pg_password'])

DATABASE_URL = (
   f"postgresql+psycopg2://{credenciais['pg_user']}:{password}"
   f"@{credenciais['pg_host']}:{credenciais['pg_port']}/{credenciais['pg_database']}"
)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
