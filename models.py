from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from pydantic import BaseModel, Field
from database import Base

class Message(BaseModel):
    message: str = Field(min_length=1)
    number: str = Field(min_length=1, max_length=30)

class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    whatsapp = Column(String, unique=True, index=True)
    is_active = Column(Boolean, default=True)