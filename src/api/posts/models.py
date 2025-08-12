from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text, func
from sqlalchemy.orm import Relationship

from src.api.db import Base


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    date_posted = Column(DateTime(), nullable=False, server_default=func.now())
    user_id = Column(ForeignKey("users.id"))

    user = Relationship("User", back_populates="posts")
