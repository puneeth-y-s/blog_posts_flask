from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Relationship
from werkzeug.security import check_password_hash, generate_password_hash

from src.api.db import Base


class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    password = Column(String, nullable=False)

    posts = Relationship("Post", back_populates="user")

    def get_password_hash(self, password):
        return generate_password_hash(password)

    def __init__(self, name, password):
        self.name = name
        self.password = self.get_password_hash(password)

    def is_password_correct(self, password):
        return check_password_hash(self.password, password)
