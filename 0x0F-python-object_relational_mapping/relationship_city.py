#!/usr/bin/python3
"""
for cities using declaraton
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_city import City
from relationship_state import Base

class City(Base):
    """ i thnk this was the problem"""
    __tablename__ = 'cities'

    id = Column(Integer, nullable=False, primary_key=True,
                autoincrement=True, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
