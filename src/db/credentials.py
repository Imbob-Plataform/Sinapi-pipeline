# src/db/credentials.py
import os
from dotenv import load_dotenv

load_dotenv()

credenciais = {
   'pg_host': os.getenv("PGHOST"),
   'pg_user': os.getenv("PGUSER"),
   'pg_port': os.getenv("PGPORT"),
   'pg_database': os.getenv("PGDATABASE"),
   'pg_password': os.getenv("PGPASSWORD")
}
