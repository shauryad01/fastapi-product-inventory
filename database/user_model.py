from sqlalchemy import Column, Integer, String, Float, DateTime
from database.product_model import Base
from sqlalchemy.sql import func

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, index=True, primary_key=True)
    email = Column(String, unique=True, index=True, nullable = False)
    password = Column(String, nullable=False)
    created_on = Column(DateTime(timezone=True), server_default=func.now())
    last_login = Column(DateTime(timezone=True), nullable=True)