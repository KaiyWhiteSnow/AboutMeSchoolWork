from sqlalchemy import Boolean, Column, DateTime, Float, ForeignKey, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Users(Base):
    __tablename__ = "Users"

    User_ID = Column(
        Integer, 
        nullable=False, 
        unique=True, 
        primary_key=True, 
        autoincrement=True
    )
    Username = Column(
        String, 
        nullable=False
    )
    Password = Column(
        String, 
        nullable=False
    )
    