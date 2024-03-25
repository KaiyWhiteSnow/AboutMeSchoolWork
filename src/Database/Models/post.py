from sqlalchemy import Boolean, Column, DateTime, Float, ForeignKey, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, unique=True, primary_key=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False)
    created_by = Column(String, nullable=False)