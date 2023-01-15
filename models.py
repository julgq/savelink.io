from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base



class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    whatsapp = Column(String, unique=True, index=True)
    is_active = Column(Boolean, default=True)

    links = relationship("Links", back_populates="user")

class Links(Base):
    __tablename__ = "links"

    id = Column(Integer, primary_key=True, index=True)
    link = Column(String)
    short = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("Users", back_populates="links")

