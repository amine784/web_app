from datetime import datetime
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, DateTime, Enum, Date



class User():
    """The User class."""
    __tablename__ = 'users'
    username = Column(String(255), unique=True, nullable=False)
    fullname = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(155), nullable=False)
    birth_date = Column(Date, nullable=False)
    
