from sqlalchemy import Column, Integer, String
from .database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    phone = Column(String, unique=True, index=True)
    password = Column(String)

class FormData(Base):
    __tablename__ = "formdata"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    value = Column(String)