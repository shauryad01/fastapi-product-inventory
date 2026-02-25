from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

DB_URL="postgresql://postgres:user@localhost:5432/demo"
engine = create_engine(DB_URL)
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

