from datetime import datetime
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, DateTime, Enum, Date



class User():
    """The User class."""
    __tablename__ = 'article'
    name = Column(String(255), unique=True, nullable=False)
    article_id = Column(String(255), nullable=False)