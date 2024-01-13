#!/usr/bin/python3
"""
a python file that contains
class definition of a State
an instance 
Base = declarative_base()
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from model_city import City

Base = declarative_base()


class State(Base):
    """definition of a State"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement=True, unique=True)
    name = Column(String(128), nullable=False)
